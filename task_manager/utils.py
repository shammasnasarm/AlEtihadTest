import os
import json
from typing import List

from constants import FILE_NAME


def load_tasks() -> List[dict]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks: List[dict]):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4, default=str)


def generate_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1