import os
import requests
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY") 

API_URL = f"https://api.github.com/repos/{REPO}/actions/runs"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def fetch_workflow_data():
    response = requests.get(API_URL, headers=headers, params={"per_page": 5})
    if response.status_code == 200:
        return response.json().get("workflow_runs", [])
    else:
        print(f"Không thể lấy dữ liệu từ GitHub API. Mã lỗi: {response.status_code}")
        return []

def generate_html(runs):
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    file_name = f"Bao_Cao_CineFlow_{current_date}.html"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Báo cáo CineFlow - {current_date}</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f8f9fa; color: #333; }}
            .container {{ max-width: 1200px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
            h1 {{ color: #24292e; text-align: center; margin-bottom: 5px; }}
            .date {{ text-align: center; color: #6a737d; margin-bottom: 30px; font-style: italic; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #e1e4e8; }}
            th {{ background-color: #24292e; color: #fff; font-weight: 600; }}
            tr:hover {{ background-color: #f6f8fa; }}
            .status {{ padding: 4px 8px; border-radius: 12px; font-weight: bold; font-size: 12px; text-transform: uppercase; }}
            .success {{ background-color: #dcffe4; color: #1a7f37; }}
            .failure {{ background-color: #ffebe9; color: #cf222e; }}
            .cancelled {{ background-color: #fff8c5; color: #9a6700; }}
            .running {{ background-color: #dbedff; color: #0969da; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>BÁO CÁO HOẠT ĐỘNG CI/CD CINEFLOW</h1>
            <div class="date">Thời gian xuất bản: {current_date}</div>
            <table>
                <thead>
                    <tr>
                        <th>Lượt chạy</th>
                        <th>Tên Luồng (Workflow)</th>
                        <th>Sự kiện Trigger</th>
                        <th>Trạng thái</th>
                        <th>Kết luận</th>
                        <th>Người kích hoạt</th>
                        <th>Thời gian khởi tạo</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for run in runs:
        conclusion = run.get('conclusion') or "running"
        if conclusion == "success":
            status_class = "success"
        elif conclusion == "failure":
            status_class = "failure"
        elif conclusion == "cancelled":
            status_class = "cancelled"
        else:
            status_class = "running"
            
        created_at = run['created_at'].replace('T', ' ').replace('Z', '')
        
        html_content += f"""
            <tr>
                <td><a href="{run['html_url']}" target="_blank" style="color: #0969da; font-weight: bold;">#{run['run_number']}</a></td>
                <td>{run['name']}</td>
                <td><code>{run['event']}</code></td>
                <td>{run['status']}</td>
                <td><span class="status {status_class}">{conclusion}</span></td>
                <td>@{run['triggering_actor']['login']}</td>
                <td>{created_at}</td>
            </tr>
        """
        
    html_content += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    
    os.makedirs("public", exist_ok=True)
    
    with open(f"public/{file_name}", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Đã tạo file báo cáo định danh: public/{file_name}")
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    runs_data = fetch_workflow_data()
    if runs_data:
        generate_html(runs_data)