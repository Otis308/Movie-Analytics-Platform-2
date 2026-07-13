import streamlit as st
from services.db import run_query

st.title("🎭 Genre Distribution")

query = """
SELECT
    genre_ids_list,
    COUNT(*) AS total_movies
FROM analytics.fact_movies
WHERE genre_ids_list IS NOT NULL
GROUP BY genre_ids_list
ORDER BY total_movies DESC
LIMIT 20
"""

df = run_query(query)

st.dataframe(df)

st.bar_chart(
    df.set_index("genre_ids_list")
)