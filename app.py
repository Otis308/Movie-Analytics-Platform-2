import streamlit as st

st.set_page_config(
    page_title="Movie Analytics Platform",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎥 Movie Analytics Platform")
st.markdown("*Centralized Data Warehouse Dashboard for Movie Metrics and Analytics.*")
st.divider()

st.subheader("📊 System & Data Overview")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Movies Analyzed", value="10,234", delta="Synced")
with col2:
    st.metric(label="Total Box Office", value="$12.5B", delta="+2.3% MoM")
with col3:
    st.metric(label="Data Pipeline Status", value="Active", delta="0 errors", delta_color="normal")
with col4:
    st.metric(label="Database", value="PostgreSQL", delta="Connected", delta_color="normal")

st.divider()

st.subheader("🧭 Analytics Modules")

c1, c2 = st.columns(2)

with c1:
    st.info("""
    **📈 Top Movies**  
    Truy vấn và xếp hạng các bộ phim dựa trên Rating, mức độ phổ biến và xu hướng hiện tại.
    """)
    
    st.warning("""
    **🎭 Popular Genres**  
    Thống kê và phân tích xu hướng thể loại phim theo từng thập kỷ hoặc khu vực.
    """)

with c2:
    st.success("""
    **💰 Revenue Analysis**  
    Biểu đồ trực quan hóa doanh thu, ROI, và phân tích tương quan ngân sách sản xuất.
    """)
    
    st.error("""
    **⭐ Actor Analysis**  
    Đánh giá hiệu suất phòng vé và tầm ảnh hưởng của các diễn viên, đạo diễn.
    """)

st.markdown("---")
