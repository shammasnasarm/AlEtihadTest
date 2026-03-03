KEYWORD_RULES: dict[str, str] = {
    "amazon": "shopping",
    "swiggy": "food",
    "salary": "income",
    "rent": "housing",
    "petrol": "transport",
}

DEFAULT_CATEGORY = "others"


def categorize(description: str) -> str:
    lowered = description.lower()
    for keyword, category in KEYWORD_RULES.items():
        if keyword in lowered:
            return category
    return DEFAULT_CATEGORY
