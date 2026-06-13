# 🎬 CineFlow: End-to-End Movie Analytics Data Platform

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon_Cloud-336791.svg)
![dbt](https://img.shields.io/badge/dbt-Analytics_Engineering-FF694B.svg)
![dlt](https://img.shields.io/badge/dlt-Data_Load_Tool-25c2a0.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF.svg)

## 📌 Tổng quan dự án (Project Overview)
**CineFlow** là một nền tảng dữ liệu tự động hóa hoàn toàn (Modern Data Stack) được thiết kế để trích xuất, xử lý và phân tích dữ liệu điện ảnh từ The Movie Database (TMDB) API. 

Dự án áp dụng quy trình **ELT (Extract - Load - Transform)** chuẩn Production, tự động hóa bằng GitHub Actions và quản lý chất lượng dữ liệu khắt khe bằng dbt, phục vụ cho mục đích phân tích xu hướng phim ảnh và doanh thu.

---

## 🏗️ Kiến trúc dữ liệu (Data Architecture)

*(Mô hình luồng dữ liệu từ lúc trích xuất đến khi trực quan hóa)*

<p align="center">
  <img src="architect_diagram.png" width="100%" alt="CineFlow Data Engineering Architecture Diagram">
</p>

### 🛠️ Tech Stack & Công cụ sử dụng
* **Nguồn dữ liệu (Source):** TMDB API
* **Điều phối & Tự động hóa (Orchestration/CI-CD):** GitHub Actions
* **Trích xuất & Tải dữ liệu (Data Ingestion - EL):** Python + `dlt` (Data Load Tool)
* **Kho dữ liệu đám mây (Cloud Data Warehouse):** Neon (Serverless PostgreSQL)
* **Chuyển đổi dữ liệu (Transformation - T):** `dbt-core` (Data Build Tool)
* **Trực quan hóa (BI & Analytics):** Metabase / Streamlit (Dự kiến)

---

## ⚙️ Luồng chạy của Pipeline (Pipeline Flow)

Dự án được lên lịch chạy tự động vào mỗi nửa đêm (00:00 UTC) với các bước sau:

1. **Extract & Load (Python + dlt):**
   * Kết nối tới TMDB API, quét qua các trang (pagination) để lấy dữ liệu phim, thể loại (genres).
   * Sử dụng thư viện `dlt` để tự động suy luận lược đồ (schema inference).
   * Áp dụng chiến lược **Incremental Loading** (Merge/Upsert) để chỉ nạp các bản ghi mới hoặc có thay đổi vào schema `raw` trên kho dữ liệu Neon PostgreSQL.

2. **Transform (dbt):**
   * Đọc dữ liệu thô từ schema `raw`.
   * Làm sạch dữ liệu, xử lý kiểu dữ liệu, loại bỏ giá trị null/trùng lặp.
   * Xây dựng mô hình dữ liệu đa chiều (Dimensional Modeling) với các bảng Dimension (`dim_movies`, `dim_genres`) và Fact (`fact_movie_popularity`).
   * Ghi các mô hình đã xử lý vào schema `analytics`, sẵn sàng cho hệ thống BI truy vấn.

3. **Data Quality & Testing:**
   * Tự động chạy các bài test của dbt (`not_null`, `unique`, `accepted_values`) để đảm bảo tính toàn vẹn của dữ liệu sau mỗi lần pipeline hoạt động.

---

## 📂 Cấu trúc thư mục (Repository Structure)

```text
CineFlow/
│
├── .github/workflows/       
│   └── cineflow_schedule.yml # Luồng CI/CD & tự động hóa bằng GitHub Actions
├── cineflow_dbt/             # Chứa toàn bộ project dbt (models, tests, profiles)
│   ├── models/
│   │   ├── staging/          # Các model làm sạch dữ liệu thô (view)
│   │   └── marts/            # Các model phân tích cuối cùng (table)
│   ├── dbt_project.yml       # Cấu hình chính của dbt
│   └── profiles.yml          # Cấu hình kết nối tới Neon Postgres
├── main.py                   # Script Python chạy dlt pipeline để EL dữ liệu
├── requirements.txt          # Danh sách thư viện Python (dlt, dbt-postgres,...)
└── README.md
