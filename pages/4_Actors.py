import streamlit as st
import plotly.express as px
from services.db import run_query

st.title("🌎 Language Analysis")

query = """
SELECT
    original_language,
    COUNT(*) AS total_movies
FROM analytics.fact_movies
GROUP BY original_language
ORDER BY total_movies DESC
LIMIT 15
"""

df = run_query(query)

fig = px.bar(
    df,
    x="original_language",
    y="total_movies",
    title="Movies by Language"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)