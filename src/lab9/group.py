import csv
from pathlib import Path

from src.lab8.models import STUDENT_FIELDS, student_from_dict, student_to_dict, validate_student

HEADER = STUDENT_FIELDS


def ensure_storage(path):
    """Creates folders and a file with a header row if the file does not exist yet."""
    path = Path(path)
    if not path.exists():
        save_students(path, [])


def _gpa_to_float(value):
    """Converts gpa from a CSV string to a float in one place."""
    if value is None or value.strip() == "":
        raise ValueError("gpa field: empty value")
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"gpa field: '{value}' is not a number")


def load_students(path):
    """Reads all records from the CSV file. Each row is processed with student_from_dict."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    students = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row")
        if set(reader.fieldnames) != set(HEADER):
            raise ValueError(
                f"invalid CSV header: {reader.fieldnames}, expected  {list(HEADER)}"
            )
        for number, row in enumerate(reader, start=2):  # row 1 is the header
            if None in row:
                raise ValueError(f"row {number}: extra columns")
            try:
                row["gpa"] = _gpa_to_float(row["gpa"])
                students.append(student_from_dict(row))
            except ValueError as e:
                raise ValueError(f"row {number}: {e}")
    return students


def save_students(path, students):
    """Overwrites the entire file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(students)


def add_student(path, student):
    """Validates the record and adds it to the end of the file."""
    validate_student(student)
    students = load_students(path)
    students.append(student_to_dict(student))
    save_students(path, students)


def list_students(path, sort_by=None):
    """Returns all students; sort_by can be None, 'fio', or 'gpa' (low to high)."""
    students = load_students(path)
    if sort_by is None:
        return students
    if sort_by not in ("fio", "gpa"):
        raise ValueError(f"unknown sort field: {sort_by}")
    return sorted(students, key=lambda s: s[sort_by])


def find_students(path, substr):
    """Returns records where substr is in the full name (Ignoring case)."""
    students = load_students(path)
    needle = substr.casefold()
    return [s for s in students if needle in s["fio"].casefold()]


def remove_student(path, fio):
    """Deletes all records with the given full name and returns the count of removed records."""
    students = load_students(path)
    kept = [s for s in students if s["fio"] != fio]
    removed = len(students) - len(kept)
    if removed > 0:
        save_students(path, kept)
    return removed


def update_student(path, fio, **fields):
    """Updates fields of the first record with the given full name. Returns True if found."""
    for key in fields:
        if key not in HEADER:
            raise KeyError(f"unknown sort field: {key}")
    students = load_students(path)
    for i in range(len(students)):
        if students[i]["fio"] == fio:
            new_rec = dict(students[i])
            new_rec.update(fields)
            students[i] = student_from_dict(new_rec)  # validate the result
            save_students(path, students)
            return True
    return False