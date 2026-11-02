import argparse

from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Data converters (JSON, CSV, XLSX)")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Convert JSON to CSV")
    p1.add_argument("--in", dest="input", required=True, help="Input .json файл")
    p1.add_argument("--out", dest="output", required=True, help="Output .csv файл")

    p2 = sub.add_parser("csv2json", help="Convert CSV to JSON")
    p2.add_argument("--in", dest="input", required=True, help="Input .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="Output .json файл")

    p3 = sub.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Input .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="Output .xlsx файл")

    args = parser.parse_args()

    if args.cmd is None:
        parser.error("A subcommand must be specified: json2csv, csv2json или csv2xlsx")

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        print(f"Done: {args.input} -> {args.output}")
    except FileNotFoundError as e:
        print(f"Error: file not found ({e})")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()