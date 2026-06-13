import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Insights", page_icon="🎬", layout="wide")
st.title("🎬 Dashboard 2: Movie Insights")

try:
    conn = st.connection("neon_db", type="sql")
    
    # Query dữ liệu cho Top 10
    df_top_rating = conn.query("""
        SELECT title, vote_average FROM analytics.fact_movies 
        WHERE vote_average IS NOT NULL AND vote_count > 100
        ORDER BY vote_average DESC LIMIT 10;
    """, ttl="10m")
    
    df_top_revenue = conn.query("""
        SELECT title, revenue FROM analytics.fact_movies 
        WHERE revenue IS NOT NULL
        ORDER BY revenue DESC LIMIT 10;
    """, ttl="10m")
    
    df_top_popularity = conn.query("""
        SELECT title, popularity FROM analytics.fact_movies 
        WHERE popularity IS NOT NULL
        ORDER BY popularity DESC LIMIT 10;
    """, ttl="10m")

    # Chia tab hiển thị mượt mà
    tab1, tab2, tab3 = st.tabs(["Top 10 Rating ⭐", "Top 10 Doanh thu 💰", "Top 10 Phổ biến 📈"])
    
    with tab1:
        st.subheader("Top 10 Phim có Điểm Đánh giá cao nhất")
        st.bar_chart(data=df_top_rating, x="title", y="vote_average")
        st.dataframe(df_top_rating, use_container_width=True)
        
    with tab2:
        st.subheader("Top 10 Phim đạt Doanh thu kỷ lục")
        st.bar_chart(data=df_top_revenue, x="title", y="revenue")
        st.dataframe(df_top_revenue, use_container_width=True)
        
    with tab3:
        st.subheader("Top 10 Phim được Săn đón/Phổ biến nhất")
        st.bar_chart(data=df_top_popularity, x="title", y="popularity")
        st.dataframe(df_top_popularity, use_container_width=True)
        
except Exception as e:
    st.error(f"Lỗi kết nối cơ sở dữ liệu: {e}")