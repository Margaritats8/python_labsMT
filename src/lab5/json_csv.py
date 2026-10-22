from pathlib import Path
import json
import csv

from src.lab4.io_txt_csv import read_text, write_csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Converts a JSON file to CSV.
    Supports a list of dictionaries [{...}, {...}], fills in missing fields with empty strings.
    UTF-8 encoding.
    The order of the columns is as in the first object.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Invalid input file format: expected .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Invalid input file format: expected .csv")
    if not json_file.exists():
        raise FileNotFoundError("The file was not found.")

    text = read_text(json_path)

    if text.strip() == "":
        raise ValueError("Empty JSON or unsupported structure")

    data = json.loads(text)
    
    if not isinstance(data, list) or not all(isinstance(value, dict) for value in data):
        raise ValueError("A list of dictionaries is expected.")
    if not data:
        raise ValueError("Empty JSON-file")
    
    header = list(data[0].keys()) 
    if len(header) == 0:
        raise ValueError("Empty JSON or unsupported structure")

    rows = []
    for item in data:
        row = []
        for column in header:
            row.append(item.get(column, ""))
        rows.append(row)

    write_csv(rows, csv_path, header=tuple(header))



def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Converts CSV to JSON (a list of dictionaries).
    The header must be present; values are saved as strings.
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    Path(json_file).parent.mkdir(parents=True, exist_ok=True)
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Invalid input file format: expected .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Invalid input file format: expected .csv")
    if not csv_file.exists():
        raise FileNotFoundError("The file was not found.")
    with csv_file.open(encoding="utf-8") as f: 
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV does not contain a title")
        data = [row for row in reader] 
    if not data:
        raise ValueError("Empty CSV")
        
    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


json_to_csv("data/samples/people.json", "data/out/people.csv")

csv_to_json("data/samples/people.csv", "data/out/people.json")

csv_to_json("data/samples/cities.csv", "data/out/cities.json")

# Пустой json файл
json_to_csv("data/samples/empty.json", "data/out/empty.csv")

# Неподдерживаемая структура
json_to_csv("data/samples/broken.json", "data/out/broken.csv")