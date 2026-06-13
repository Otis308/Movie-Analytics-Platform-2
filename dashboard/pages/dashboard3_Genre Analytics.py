import streamlit as st
import pandas as pd

st.set_page_config(page_title="Genre Analytics", page_icon="📈", layout="wide")
st.title("📈 Dashboard 3: Genre Analytics")

try:
    conn = st.connection("neon_db", type="sql")
    
    # Query dữ liệu nhóm phân tích theo thể loại phim
    df_genre = conn.query("""
        SELECT 
            genre_name,
            SUM(revenue) as total_revenue,
            AVG(vote_average) as avg_rating,
            COUNT(*) as movie_count
        FROM analytics.movie_performance_mart
        WHERE genre_name IS NOT NULL
        GROUP BY genre_name
        ORDER BY total_revenue DESC;
    """, ttl="10m")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tổng Doanh thu theo Thể loại")
        st.bar_chart(data=df_genre, x="genre_name", y="total_revenue")
        
        st.subheader("Số lượng Phim phân bổ theo Thể loại")
        st.bar_chart(data=df_genre, x="genre_name", y="movie_count")
        
    with col2:
        st.subheader("Đánh giá (Rating) trung bình theo Thể loại")
        st.line_chart(data=df_genre, x="genre_name", y="avg_rating")
        
        st.subheader("Bảng dữ liệu tổng hợp chi tiết")
        st.dataframe(df_genre, use_container_width=True)
        
except Exception as e:
    st.error(f"Lỗi kết nối cơ sở dữ liệu: {e}")