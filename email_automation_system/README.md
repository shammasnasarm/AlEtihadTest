# Email Automation System

Reads a contacts CSV and an HTML email template, personalises each message via Python `.format()`, sends via SMTP, and repeats daily at a scheduled time.

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file with your SMTP credentials
cp .env.template .env
# Fill values in .env (SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SCHEDULE_TIME)

# 4. Run the scheduler
python main.py --csv contacts.csv --template template.html
# Emails are sent daily at SCHEDULE_TIME. Press Ctrl+C to stop.
```

---

## Input Files

### `contacts.csv`

Must include columns: `email`, `subject` (and any variables used in the template).

```
email,subject,name
alice@example.com,Welcome Alice!,Alice
bob@example.com,Welcome Bob!,Bob
```

### `templates/template.html`

```html
<p>Hello {name},</p>
<p>Welcome to our platform!</p>
```

---

## Why I went with this approach

- Simple to implement
- Just need a Gmail account to send email
- Good for internal purpose

---

## Further approach

- Use **AWS EventBridge** for scheduling
- Use **AWS SES** for sending emails
- Use **SES templates** for dynamic/personalized email content
- Add logging/monitoring and retry handling
