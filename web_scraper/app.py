from flask import Flask, render_template, request
import json
import os

from scraper import scrape_jobs, JOBS_FILE
from utils import compute_stats

app = Flask(__name__)


def load_jobs():
    if os.path.exists(JOBS_FILE):
        with open(JOBS_FILE, "r") as f:
            return json.load(f)
    return []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        scrape_jobs(query)

    jobs = load_jobs()
    stats = compute_stats(jobs)
    return render_template("index.html", jobs=jobs, stats=stats)


if __name__ == "__main__":
    app.run(debug=True)