import datetime
import requests


def fetch_jobs(keyword="data"):
    '''
    Fetches jobs based on the keywords that are inserted
    ''' 
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jobs = response.json()

        results = []
        for job in jobs:
            # Skip metadata headers in API
            if not isinstance(job, dict):
                continue

            position = job.get("position", "")
            if keyword.lower() in position.lower():
                results.append({
                    "title": job.get("position"),
                    "company": job.get("company"),
                    "location": job.get("location"),
                    "url": job.get("url"),
                    "date": datetime.datetime.utcnow().strftime("%Y-%m-%d")
                })

        return results

    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []
    
    
    
if __name__ == "__main__":
    jobs = fetch_jobs()
    for j in jobs:
        print(j)
