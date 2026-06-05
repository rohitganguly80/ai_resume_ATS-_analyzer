import sqlite3
import pandas as pd

DB_NAME = "ats_history.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ATS_ANALYSIS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_name TEXT,
        ats_score INTEGER,
        match_percentage INTEGER,
        analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(
        resume_name,
        ats_score,
        match_percentage):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ATS_ANALYSIS
    (
        resume_name,
        ats_score,
        match_percentage
    )
    VALUES (?, ?, ?)
    """,
    (
        resume_name,
        ats_score,
        match_percentage
    ))

    conn.commit()
    conn.close()


def get_all_analysis():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM ATS_ANALYSIS",
        conn
    )

    conn.close()

    return df