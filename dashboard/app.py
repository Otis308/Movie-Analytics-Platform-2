import streamlit as st

st.set_page_config(page_title="CineFlow Data Platform", page_icon="🎬", layout="wide")

st.title("🎬 Welcome to CineFlow Data Platform")
st.markdown("""
### Nền tảng Phân tích Dữ liệu Điện ảnh Toàn diện (End-to-End Movie Analytics)
    
Hệ thống này trực quan hóa kho dữ liệu được tự động hóa hoàn toàn qua quy trình **ELT Production**:
`TMDB API ➡️ Python + dlt ➡️ Neon PostgreSQL (Raw) ➡️ dbt (Transform) ➡️ Streamlit (BI)`
    
👈 **HƯỚNG DẪN:** Bạn hãy nhìn sang thanh điều hướng bên trái (Sidebar) và chọn Dashboard muốn xem để bắt đầu khám phá dữ liệu!
    
---
*Hệ thống được giám sát và vận hành tự động theo lịch trình bằng GitHub Actions.*
""")