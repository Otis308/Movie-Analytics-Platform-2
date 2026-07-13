import streamlit as st
import plotly.express as px
from services.db import run_query

st.title("🎬 Top Movies")

query = """
SELECT
    title,
    vote_average,
    vote_count,
    popularity
FROM analytics.fact_movies
WHERE vote_count > 50
ORDER BY vote_average DESC
LIMIT 10
"""

df = run_query(query)

st.dataframe(df)

fig = px.bar(
    df,
    x="title",
    y="vote_average",
    hover_data=["vote_count", "popularity"],
    title="Top Rated Movies"
)

st.plotly_chart(fig, use_container_width=True)