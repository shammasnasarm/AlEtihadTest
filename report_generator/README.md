# Report Generator

Reads a JSON or CSV input file containing user records and generates a personalized PDF report for each user using ReportLab.

---

## Project Structure

    report_generator/
    │
    ├── main.py
    ├── utils.py
    ├── constants.py
    ├── requirements.txt
    └── input/
        └── user.json

Generated PDFs are saved to `output/` (created automatically).

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run with a JSON or CSV file placed inside the input/ folder
python main.py --file user.json
```

---

## Input Format

### JSON (`input/user.json`)

```json
[
    {
        "name": "Shammas Nasar",
        "email": "shammas@example.com",
        "score": 88,
        "department": "Engineering"
    }
]
```

### CSV (`input/users.csv`)

```
name,email,score,department
Shammas Nasar,shammas@example.com,88,Engineering
```

---

## Output

Each user gets a separate PDF file saved to `output/`:

```
output/Shammas_Nasar_report.pdf
```

Each PDF includes:

- Name, Email, Department, Score
- A formatted table with all fields

---

## Further approach

- Add HTML template support using `Jinja2` + `WeasyPrint`
- Bulk generation with parallel processing for large datasets
