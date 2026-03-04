# Web Scraper

A Flask web app that scrapes job listings from [infopark.in](https://infopark.in/companies/job-search) based on a search query, filters by matched skills, saves results to JSON, and displays them in an HTML dashboard.

---

## Project Structure

    web_scraper/
    │
    ├── app.py
    ├── scraper.py
    ├── utils.py
    ├── requirements.txt
    └── templates/
        └── index.html

Scraped jobs are saved to `data/jobs.json` (created automatically).

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# Open: http://127.0.0.1:5000
```

Enter a job search query in the form (e.g. `python developer`) and submit to trigger the scrape.

---

## How it works

- Scrapes paginated job listings from `infopark.in` using `requests` + `BeautifulSoup`
- For each job, fetches the detail page and checks for matched skills
- Only jobs with at least one matched skill are saved
- Results are stored in `data/jobs.json`
- Dashboard shows stats: total jobs, posted today, expiring within 7 days

---

## Matched Skills Filter

Jobs are kept only if the job description contains at least one of:

```
python, django, flask, sql, postgresql, mongodb, redis,
rabbitmq, kafka, docker, kubernetes, aws, azure, gcp,
oracle, mysql, sqlite
```

---

> **Note:**  
> This scraper does **not** support direct access to sites like LinkedIn or Indeed, as scraping them requires an official API key and/or violates their terms of service.  
> This project is intended for public job boards (such as infopark.in) that do not require authentication or proprietary access.