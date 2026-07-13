import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password=os.getenv("DB_PASSWORD_NEON"),
        host="ep-still-bread-aow0faf8.c-2.ap-southeast-1.aws.neon.tech",
        port="5432",
        sslmode="require"
    )

def run_query(sql):
    conn = get_connection()

    df = pd.read_sql(sql, conn)

    conn.close()

    return df