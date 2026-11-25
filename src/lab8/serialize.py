import json
from pathlib import Path

from src.lab8.models import student_to_dict, student_from_dict, format_student


def students_to_json(students, path):
    """Saves a list of records to JSON. """
    data = [student_to_dict(s) for s in students]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    """Reads a JSON array and returns a list of valid records.

    Policy: broken records are skipped; at the end it prints
    how many were skipped and why.
    """
    if not Path(path).is_file():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of records")

    students = []
    errors = []
    for number, item in enumerate(data, start=1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            errors.append(f"record #{number}: {e}")

    if errors:
        print(f"Skipped records: {len(errors)}")
        for message in errors:
            print(f"  - {message}")
    return students


def main():
   
    students = students_from_json("data/lab8/good_input.json")
    for s in students:
        print(format_student(s))
    students_to_json(students, "data/lab8/good_output.json")
    print("Written:", len(students), "records to students_output.json")


    good = students_from_json("data/lab8/bad_input.json")
    print("Valid records read:", len(good))


if __name__ == "__main__":
    main()