import os
import argparse

from constants import INPUT_FOLDER
from utils import load_data, create_pdf



def main():
    parser = argparse.ArgumentParser(description="Generate personalized PDF reports")
    parser.add_argument("--file", required=True, help="Path to input JSON or CSV file")

    args = parser.parse_args()
    input_file = os.path.join(INPUT_FOLDER, args.file)

    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist")
        return

    data = load_data(input_file)

    for user in data:
        create_pdf(user)


if __name__ == "__main__":
    main()