import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="finance_tracker",
        description="Personal Finance Tracker CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    import_parser = subparsers.add_parser("import", help="Import transactions from a CSV file")
    import_parser.add_argument("--file", required=True, help="Path to the CSV file")

    report_parser = subparsers.add_parser("report", help="Generate a monthly financial report")
    report_parser.add_argument(
        "--month",
        required=True,
        help="Month in YYYY-MM format (e.g. 2026-02)",
    )

    args = parser.parse_args()

    if args.command == "import":
        from utils.importer import import_csv
        import_csv(args.file)

    elif args.command == "report":
        from utils.report import generate_monthly_report
        generate_monthly_report(args.month)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
