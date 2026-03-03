from schemas import Task
from utils import load_tasks, save_tasks, generate_id
from datetime import datetime
from pydantic import ValidationError


def create_task(args):
    tasks = load_tasks()

    try:
        task = Task(
            id=generate_id(tasks),
            title=args.title,
            description=args.description,
            due_date=args.due,
            is_done=False,
            created_at=datetime.now(),
        )
    except ValidationError as e:
        print("Validation Error")
        print(e)
        return

    tasks.append(task.model_dump())
    save_tasks(tasks)
    print("Task created successfully")


def list_tasks(args):
    tasks = [Task(**t) for t in load_tasks()]

    if not args.all:
        tasks = [t for t in tasks if not t.is_done]

    if args.due:
        today = datetime.now().date()
        if args.due == "today":
            tasks = [t for t in tasks if t.due_date == today]

        elif args.due == "overdue":
            tasks = [t for t in tasks if t.due_date and t.due_date < today and not t.is_done]

        elif args.due == "upcoming":
            tasks = [t for t in tasks if t.due_date and t.due_date > today]

    if not tasks:
        print("No tasks found.")
        return

    tasks.sort(key=lambda x: (x.due_date is None, x.due_date))

    for t in tasks:
        print(f"[{t.id}] {t.title} | Due: {t.due_date} | Done: {t.is_done}")


def mark_done(args):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == args.id:
            t["is_done"] = True
            save_tasks(tasks)
            print("Task marked as done")
            return

    print("Task not found")


def delete_task(args):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != args.id]

    if len(new_tasks) == len(tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print("Task deleted successfully")


def edit_task(args):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == args.id:
            if args.title:
                t["title"] = args.title
            if args.description:
                t["description"] = args.description
            if args.due:
                t["due_date"] = args.due

            save_tasks(tasks)
            print("Task updated successfully")
            return

    print("Task not found")
