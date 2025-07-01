import sqlite3

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT UNIQUE,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_jobs(jobs):
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    for job in jobs:
        try:
            c.execute("INSERT INTO jobs (title, company, location, url, date) VALUES (?, ?, ?, ?, ?)",
                      (job['title'], job['company'], job['location'], job['url'], job['date']))
        except sqlite3.IntegrityError:
            # Skip duplicates based on unique job URL
            continue

    conn.commit()
    conn.close()