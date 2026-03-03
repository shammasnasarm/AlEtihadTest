import argparse
import os

from services import create_task, list_tasks, mark_done, delete_task, edit_task

from constants import FILE_NAME


def main():
    os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)
    parser = argparse.ArgumentParser(prog="task-manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create
    p_create = subparsers.add_parser("create")
    p_create.add_argument("--title", required=True)
    p_create.add_argument("--description")
    p_create.add_argument("--due")
    p_create.set_defaults(func=create_task)

    # list
    p_list = subparsers.add_parser("list")
    p_list.add_argument("--all", action="store_true")
    p_list.add_argument("--due", choices=["today", "overdue", "upcoming"],
                        help="Filter by due status"
    )
    p_list.set_defaults(func=list_tasks)

    # done
    p_done = subparsers.add_parser("done")
    p_done.add_argument("--id", type=int, required=True)
    p_done.set_defaults(func=mark_done)

    # delete
    p_delete = subparsers.add_parser("delete")
    p_delete.add_argument("--id", type=int, required=True)
    p_delete.set_defaults(func=delete_task)

    # edit
    p_edit = subparsers.add_parser("edit")
    p_edit.add_argument("--id", type=int, required=True)
    p_edit.add_argument("--title")
    p_edit.add_argument("--description")
    p_edit.add_argument("--due")
    p_edit.set_defaults(func=edit_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()