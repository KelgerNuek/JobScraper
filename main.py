from scraper.scraper import fetch_jobs
from storage.db import init_db, save_jobs
from notifier.emailer import send_email

def run():
    print("Starting job scraper...")
    init_db()
    jobs = fetch_jobs()
    save_jobs(jobs)
    send_email(jobs)

if __name__ == "__main__":
    run()
