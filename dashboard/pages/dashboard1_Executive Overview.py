import streamlit as st
import pandas as pd

st.set_page_config(page_title="Executive Overview", page_icon="📊", layout="wide")
st.title("📊 Dashboard 1: Executive Overview")

try:
    conn = st.connection("neon_db", type="sql")
    
    # Query các chỉ số KPI từ mô hình dbt marts tổng hợp
    df_metrics = conn.query("""
        SELECT 
            COUNT(DISTINCT title) as total_movies,
            SUM(revenue) as total_revenue,
            AVG(vote_average) as avg_rating
        FROM analytics.movie_performance_mart;
    """, ttl="10m")
    
    # Query thể loại phổ biến nhất
    df_popular_genre = conn.query("""
        SELECT genre_name, COUNT(*) as count
        FROM analytics.movie_performance_mart
        WHERE genre_name IS NOT NULL
        GROUP BY genre_name
        ORDER BY count DESC
        LIMIT 1;
    """, ttl="10m")

    # Hiển thị các thẻ KPI số liệu lớn
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tổng số phim", f"{df_metrics['total_movies'][0]:,}")
    with col2:
        total_rev = df_metrics['total_revenue'][0] if df_metrics['total_revenue'][0] else 0
        st.metric("Tổng doanh thu", f"${total_rev:,.2f}")
    with col3:
        avg_rate = df_metrics['avg_rating'][0] if df_metrics['avg_rating'][0] else 0
        st.metric("Rating trung bình", f"{round(avg_rate, 2)} ⭐")
    with col4:
        popular_genre = df_popular_genre['genre_name'][0] if not df_popular_genre.empty else "N/A"
        st.metric("Genre phổ biến nhất", popular_genre)

    st.markdown("---")
    st.info("💡 Mẹo dành cho nhà tuyển dụng: Dữ liệu KPI trên được đồng bộ trực tiếp từ Analytics Schema do dbt sinh ra trên Neon Cloud.")
    
except Exception as e:
    st.error(f"Lỗi kết nối cơ sở dữ liệu: {e}")