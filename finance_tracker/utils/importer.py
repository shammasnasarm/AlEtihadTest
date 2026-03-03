import json
from pathlib import Path

import pandas as pd
from pydantic import ValidationError

from schemas import Transaction
from utils.categorizer import categorize

CHUNK_SIZE = 1000
DATA_FILE = Path.cwd() / "data" / "transactions.json"


def _load() -> list[dict]:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def _save(transactions: list[dict]) -> None:
    DATA_FILE.write_text(
        json.dumps(transactions, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

def import_csv(file_path: str) -> None:
    path = Path(file_path)
    if not path.exists():
        print(f"==== File not found: {file_path} ====")
        return

    total_imported = 0
    total_skipped = 0
    chunk_index = 0

    reader = pd.read_csv(path, chunksize=CHUNK_SIZE)

    for chunk in reader:
        chunk_index += 1
        print(f"==== Processing chunk {chunk_index} ({len(chunk)} rows)...")
        chunk = chunk[chunk["amount"] != 0]

        chunk["description"] = chunk["description"].str.strip()
        chunk["category"] = chunk["description"].apply(categorize)

        valid_transactions: list[Transaction] = []

        for _, row in chunk.iterrows():
            try:
                transaction = Transaction(
                    date=row["date"],
                    description=row["description"],
                    amount=row["amount"],
                    category=row["category"],
                )
                valid_transactions.append(transaction)
            except ValidationError as e:
                total_skipped += 1
                print(f"=> Invalid row ({row.to_dict()}): {e.errors()[0]['msg']}")

        if valid_transactions:
            existing = _load()
            existing.extend([t.model_dump(mode="json") for t in valid_transactions])
            _save(existing)
            total_imported += len(valid_transactions)
            print(f"=> Chunk {chunk_index}: saved {len(valid_transactions)} transactions.")

    print(f"===== Import complete. Imported: {total_imported} | Skipped: {total_skipped} =====")
