import streamlit as st
import plotly.express as px
from services.db import run_query

st.title("📈 Movie Release Trends")

query = """
SELECT
    EXTRACT(YEAR FROM release_date) AS year,
    COUNT(*) AS total_movies,
    AVG(popularity) AS avg_popularity
FROM analytics.fact_movies
WHERE release_date IS NOT NULL
GROUP BY year
ORDER BY year
"""

df = run_query(query)

fig = px.line(
    df,
    x="year",
    y="total_movies",
    markers=True,
    title="Movies Released Per Year"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)