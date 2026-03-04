# Task Manager

A CLI task manager to create, list, edit, complete, and delete tasks — persisted to a local JSON file (`data/tasks.json`).

---

## Project Structure

    task_manager/
    │
    ├── main.py
    ├── services.py
    ├── schemas.py
    ├── utils.py
    ├── constants.py
    └── requirements.txt

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
```

---

## Commands

### Create a task

```bash
python main.py create --title "Buy groceries" --description "Milk, eggs" --due 2026-03-10
```

### List tasks

```bash
# All tasks (including done)
python main.py list --all

# Filter by due status
python main.py list --due today
python main.py list --due overdue
python main.py list --due upcoming
```

### Mark as done

```bash
python main.py done --id 1
```

### Edit a task

```bash
python main.py edit --id 1 --title "Updated title" --due 2026-03-15
```

### Delete a task

```bash
python main.py delete --id 1
```

---

## Task Fields

| Field | Required | Description |
|---|---|---|
| `--title` | Yes | Task title (max 100 chars) |
| `--description` | No | Optional description |
| `--due` | No | Due date in `YYYY-MM-DD` format |

---

## Why I use this approach

This approach ensures data integrity by validating input with Pydantic, clearly separates business logic from CLI commands for better maintainability, and makes it easy to extend functionality (such as adding new commands or automating workflows).

