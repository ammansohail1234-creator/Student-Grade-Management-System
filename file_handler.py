
import json
from pathlib import Path

# Create the file path in the project folder
FILE_PATH = Path(__file__).with_name("students.json")


def load_students():
    """Load student records from JSON."""

    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student records.")
        return []


def save_students(students):
    """Save student records to JSON."""

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
