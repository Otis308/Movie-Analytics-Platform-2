import os
import sys
import requests
import json
import datetime
import dlt
from pathlib import Path
from dotenv import load_dotenv

#Ghi log tiến trình
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))
from src.utils.logger import get_logger
logger = get_logger("Extract_TMDB_Movies")

#Lấy dữ liệu từ file .env
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
AUTH_KEY = os.getenv("TMDB_API_AUTH")
DATABASE_URL = os.getenv("DATABASE_URL")

if not API_KEY: 
    raise ValueError("TMDB_API_KEY is not find from .env")
if not AUTH_KEY: 
    raise ValueError("TMDB_API_AUTH is not find from .env")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not find from .env")

#Hàm extract data từ TMDB lấy Discover/Movie
@dlt.resource(name="tmdb_discover_movies", write_disposition="merge", primary_key="id")
def get_data_movies(start_page=1, end_page=5):

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {AUTH_KEY}"
    }

    # 1. Setup thư mục raw một lần ở ngoài vòng lặp
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    partition_folder = f"load_date={current_date}"

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_script_dir))
    raw_dir = os.path.join(project_root, "data", "raw", "movies", partition_folder)
    os.makedirs(raw_dir, exist_ok=True)
    
    # 2. Vòng lặp duyệt qua các trang
    for page_num in range(start_page, end_page + 1):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page_num}&sort_by=popularity.desc"
        logger.info(f"Đang tải dữ liệu trang {page_num}...")

        try:
            response = requests.get(
                url, 
                headers=headers, 
                timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            continue

        data = response.json()

        file_path = os.path.join(raw_dir, f"raw_discover_movies_page_{page_num}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Đã lưu file raw cục bộ tại: {file_path}")
    
        movies_list = data.get('results', [])

        if not movies_list:
            print("Erorr!!! Đã hết dữ liệu từ API.")
            break
        
        load_timestamp = datetime.datetime.utcnow().isoformat()
        for movie in movies_list:
            movie["_loaded_at"] = load_timestamp
            movie["_page"] = page_num
        yield movies_list 

# pipeline
pipeline = dlt.pipeline(
    pipeline_name="tmdb_data",
    dataset_name="raw_movies_data",
    destination=dlt.destinations.postgres(credentials=DATABASE_URL), 
)
