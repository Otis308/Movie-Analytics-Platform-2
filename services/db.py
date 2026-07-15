import os
import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_secret(key):
    if key in os.environ:
        return os.environ[key]
    return st.secrets[key]

def get_connection():
    return psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password=get_secret("DB_PASSWORD_NEON"),
        host="ep-still-bread-aow0faf8.c-2.ap-southeast-1.aws.neon.tech",
        port="5432",
        sslmode="require"
    )

def run_query(sql):
    with get_connection() as conn:
        return pd.read_sql(sql, conn)