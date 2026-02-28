import argparse
import csv
import smtplib
import schedule
import time
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SCHEDULE_TIME = os.getenv("SCHEDULE_TIME", "09:00")


def send_email(to_email, subject, html_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)


def send_bulk_emails(csv_file, template_file):
    # Load template
    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()

    # Read CSV
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            to_email = row["email"]
            subject = row["subject"]
            message = template.format(**row)

            send_email(
                to_email=to_email,
                subject=subject,
                html_body=message
            )

            print(f"Sent to {to_email}")



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="CSV file name")
    parser.add_argument("--template", required=True, help="Template file name")

    args = parser.parse_args()

    csv_file = args.csv
    template_file = os.path.join("templates", args.template)

    if not os.path.exists(template_file):
        print(f"Template not found: {template_file}")
        sys.exit(1)

    if not os.path.exists(csv_file):
        print(f"CSV file not found: {csv_file}")
        sys.exit(1)


    schedule.every().day.at(SCHEDULE_TIME).do(
        send_bulk_emails, csv_file=csv_file, template_file=template_file
    )

    print("----Scheduler started...----")

    while True:
        schedule.run_pending()
        time.sleep(60)
