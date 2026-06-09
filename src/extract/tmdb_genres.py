import os
import requests
import json
from dotenv import load_dotenv
import dlt
from dlt.sources.helpers import requests

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
AUTH_KEY = os.getenv("TMDB_API_AUTH")
if not API_KEY: 
    raise ValueError("TMDB_API_KEY is not find from .env")
if not AUTH_KEY: 
    raise ValueError("TMDB_API_AUTH is not find from .env")

@dlt.resource(name="tmdb_discover_movies", write_disposition="replace")
def get_data_movies():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {AUTH_KEY}"
    }

    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_script_dir))
    raw_dir = os.path.join(project_root, "data", "raw", "movies")
    os.makedirs(raw_dir, exist_ok=True)
    
    file_path = os.path.join(raw_dir, "raw_discover_movies_page_1.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Đã lưu file raw cục bộ tại: {file_path}")
    
    movies_list = data.get('results', [])
    
    yield movies_list 

# pipeline
pipeline = dlt.pipeline(
    pipeline_name="tmdb_data",
    destination="postgres", 
    dataset_name="raw_movies_data"
)

if __name__ == "__main__":
    print("🚀 Bắt đầu tiến trình ELT đẩy dữ liệu vào PostgreSQL...")
    load_info = pipeline.run(get_data_movies())
    
    print(load_info)