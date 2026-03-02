import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import time


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://infopark.in/companies/job-search?search={}&page={}"

JOBS_FILE = os.path.join("data", "jobs.json")

REQUIRED_SKILLS = [
    "python", "django", "flask", "sql", "postgresql", "mongodb", "redis",
    "rabbitmq", "kafka", "docker", "kubernetes", "aws", "azure", "gcp",
    "oracle", "mysql", "sqlite"
]

os.makedirs(os.path.dirname(JOBS_FILE), exist_ok=True)


def scrape_jobs(query="python developer"):
    page = 1
    query = query.replace(" ", "+")

    jobs = []

    while True:
        print(f"---- Scraping page {page} ----")
        url = BASE_URL.format(query, page)
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        jobs_table_sec = soup.select_one("#job-list")
        job_table = jobs_table_sec.select_one("table")
        job_rows = job_table.select("tr")

        no_more_pages = False
        for card in job_rows:
            cols = card.find_all("td")
            if len(cols) == 0:
                continue

            if cols[0].text.strip().lower() == "no jobs.":
                no_more_pages = True
                break

            post_date = cols[0]
            title = cols[1]
            company = cols[2]
            last_date = cols[3]
            link = cols[4].find("a")
            job_details_response = requests.get(link.get("href"), headers=HEADERS)
            detail_soup = BeautifulSoup(job_details_response.text, "html.parser")
            job_description = detail_soup.select_one(".deatil-box").text.strip()
            matched_skills = list(set(skill for skill in REQUIRED_SKILLS if skill in job_description.lower()))
            if not matched_skills:
                continue

            job_data = {
                "title": title.text.strip() if title else "",
                "company": company.text.strip() if company else "",
                "posted": post_date.text.strip() if post_date else "",
                "last_date": last_date.text.strip() if last_date else "",
                "link": link.get("href") if link else "",
                "skills": matched_skills,
                "scraped_at": datetime.utcnow().isoformat()
            }

            jobs.append(job_data)
            time.sleep(1)

        if no_more_pages:
            break

        page += 1
        time.sleep(1)

    with open(JOBS_FILE, "w") as f:
        json.dump(jobs, f, indent=4)

    return jobs

# if __name__ == "__main__":
#     jobs = scrape_jobs("python developer")
#     print(f"Scraped {len(jobs)} jobs")
