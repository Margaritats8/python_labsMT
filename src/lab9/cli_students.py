import argparse
import sys

from src.lab8.models import make_student, format_student
from src.lab9.group import ensure_storage, add_student, list_students, find_students, remove_student, update_student

DEFAULT_DB = "data/lab9/students.csv"


def fail(message):
    """Prints an error to stderr and exits the program with code 1."""
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    # общий параметр --db для всех подкоманд
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--db", default=DEFAULT_DB, help=f"path to CSV storage (default:{DEFAULT_DB})")

    parser = argparse.ArgumentParser(description="CLI for student storage (CSV)")
    sub = parser.add_subparsers(dest="cmd")

    p = sub.add_parser("add", parents=[common], help="Add a student")
    p.add_argument("--fio", required=True)
    p.add_argument("--birthdate", required=True, help="YYYY-MM-DD")
    p.add_argument("--group", required=True)
    p.add_argument("--gpa", type=float, required=True, help="from 0 to 5")

    p = sub.add_parser("list", parents=[common], help="List all students")
    p.add_argument("--sort", choices=["fio", "gpa"], help="sort order")

    p = sub.add_parser("find", parents=[common], help="Search by substring in full name")
    p.add_argument("--q", required=True, help="substring (Ignoring case)")

    p = sub.add_parser("remove", parents=[common], help="Remove a student by full name")
    p.add_argument("--fio", required=True)

    p = sub.add_parser("update", parents=[common], help="Update student fields")
    p.add_argument("--fio", required=True)
    p.add_argument("--gpa", type=float)
    p.add_argument("--group")
    p.add_argument("--birthdate")

    args = parser.parse_args()
    if args.cmd is None:
        parser.error("Please specify a subcommand: add, list, find, remove, or update")

    try:
        ensure_storage(args.db)

        if args.cmd == "add":
            student = make_student(args.fio, args.birthdate, args.group, args.gpa)
            add_student(args.db, student)
            print(f"Added: {format_student(student)}")

        elif args.cmd == "list":
            students = list_students(args.db, args.sort)
            if not students:
                print("No students found")
            for s in students:
                print(format_student(s))

        elif args.cmd == "find":
            students = find_students(args.db, args.q)
            if not students:
                print("Nothing found")
            for s in students:
                print(format_student(s))

        elif args.cmd == "remove":
            print(f"Records removed: {remove_student(args.db, args.fio)}")

        elif args.cmd == "update":
            fields = {}
            if args.gpa is not None:
                fields["gpa"] = args.gpa
            if args.group is not None:
                fields["group"] = args.group
            if args.birthdate is not None:
                fields["birthdate"] = args.birthdate
            if not fields:
                parser.error("specify at least one field to update: --gpa, --group, or --birthdate")
            if update_student(args.db, args.fio, **fields):
                print(f"Обновлено: {args.fio}")
            else:
                fail(f"студент не найден: {args.fio}")

    except KeyError as e:
        fail(e.args[0])
    except (ValueError, FileNotFoundError) as e:
        fail(e)


if __name__ == "__main__":
    main()