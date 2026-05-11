import requests

URL = "https://remoteok.com/api"


def scrape_jobs():
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    jobs = []

    for item in data[1:]:  # skip metadata row
        jobs.append({
            "title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location"),
            "url": item.get("url"),
        })

    return jobs


if __name__ == "__main__":
    jobs = scrape_jobs()
    print(f"Scraped {len(jobs)} jobs")
    print(jobs[0])