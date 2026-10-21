# ЛР5 - JSON и конвертации (JSON↔CSV, CSV→XLSX)
### Задание А

### json_to_csv
``` python 
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


```

1. Скрипт проверяет расширения файлов (.json и .csv) и физическое наличие исходного файла на диске. При ошибке генерирует ValueError или FileNotFoundError.
2. Файл считывается в строку функцией read_text. Если после удаления пробелов методом .strip() строка пустая — вызывается ValueError.
3. Строка переводится в объект Python через json.loads(). Скрипт проверяет, что получен именно список словарей [{}, {}], иначе выдает ValueError.
4. Ключи самого первого словаря в списке (data[0].keys()) берутся в качестве названий колонок таблицы.
5. Скрипт перебирает все словари и вытаскивает значения строго по порядку заголовков. Если в каком-то словаре нет нужного ключа, метод .get(column, "") автоматически вставляет пустую строку. Это защищает таблицу от перекосов.
6. Сформированная таблица (массив строк и заголовки) передается в функцию write_csv для записи на диск в кодировке UTF-8.

### csv_to_json

```python 
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

```

1. Сверяем расширения (.csv и .json), ищем исходный файл на диске и создаем папку для сохранения результата. При любых несоответствиях программа выдает ошибку.
2. Таблица открывается в кодировке utf-8. Через инструмент csv.DictReader верхняя строка автоматически становится ключами, а все последующие строки превращаются в удобные Python-словари.
3. Программа проверяет наличие шапки таблицы (reader.fieldnames). Если названий у колонок нет, выполнение прерывается с ошибкой.
4. Все строки-словари циклом упаковываются в один общий список. Если на этом этапе список оказался пустым, скрипт выдает ошибку.
5. Данные переводятся в JSON-формат. Чтобы русский текст не превратился в непонятные коды, отключается экранирование символов, а для красивого визуального отображения выставляются отступы в два пробела.

### Задание В

### сsv_to_xlsx
```python
import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Converts CSV to XLSX.

     The first line of the CSV is the header. The sheet is named “Sheet1”. 
     The width of each column is equal to the length of the longest value, but not less than 8 characters.
     Values are written as strings (types are not guessed).

     Raises:
     FileNotFoundError: no input CSV.
     ValueError: invalid extension, empty CSV.
    """
    src = Path(csv_path)
    dst = Path(xlsx_path)
    if src.suffix.lower() != ".csv":
        raise ValueError(f"Invalid file type: expected .csv, received '{src.suffix}'")
    if dst.suffix.lower() != ".xlsx":
        raise ValueError(f"Invalid file type: expected .xlsx, received '{dst.suffix}'")
    if not src.is_file():
        raise FileNotFoundError(f"The file was not found: {csv_path}")

    rows = []
    with open(csv_path, encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if row:
                rows.append(row)

    if len(rows) < 2:
        raise ValueError("CSV пустой или в нём нет данных (только заголовок)")

    widths = {}
    for row in rows:
        for index, cell in enumerate(row):
            if len(cell) > widths.get(index, 0): 
                widths[index] = len(cell)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)

    for index, width in widths.items():
        letter = get_column_letter(index + 1)
        ws.column_dimensions[letter].width = max(8, width)

    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)

```

1. Проверка путей и расширений: строгий контроль типов (.csv → .xlsx) и наличия входного файла; иначе ValueError и FileNotFoundError.
2. Чтение строк: текстовый режим, csv.reader() построчно собирает данные в rows, пропуская пустые элементы.
3. Контроль данных: нужно ≥ 2 строки (заголовки + данные), иначе ValueError.
4. Ширина столбцов: проход по ячейкам, в словаре widths сохраняется длина самого длинного текста для каждого столбца.
5. Создание книги: Workbook из openpyxl, активный лист "Sheet1", строки добавляются через ws.append().
6. Подгонка ячеек: цикл по widths, индексы в буквы формта Excel (0 -> А) через get_column_letter(), ширина = max(8, width) по тз.
7. Сохранение: файл записывается по указанному пути.

### Обработка ошибок

1. Отсутствие входного файла FileNotFoundError.
2. Неверный тип файла ValueError: расширение входного и выходного файла проверяется (.json, .csv, .xlsx).
3. Пустой JSON или неподдерживаемая структура (ValueError): пустой файл/список/словарь, список с не-словарями или объектами без ключей.
4. Пустой CSV или CSV без данных (ValueError): пустой файл, файл только с заголовком, пустые или повторяющиеся имена колонок, строка с большим числом значений, чем в заголовке.
5. Разные ключи в JSON: колонки CSV — объединение всех ключей, недостающие значения заполняются пустыми строками.
6. Типы данных: при CSV → JSON все значения остаются строками, а при JSON -> CSV вложенные списки и словари записываются в ячейку как JSON-строка и обратно в структуру не восстанавливаются.

## Способ запуска

Запуск выполняется из корня репозитория с помощью `-m`. Для задания B необходима openpyxl:

```
pip install openpyxl
```

Использование функций из кода:

```python
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

json_to_csv("data/samples/people.json", "data/out/people.csv")
csv_to_json("data/samples/people.csv", "data/out/people.json")
csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
```

## Проверка результатов

### 1. JSON -> CSV
![вывод 1](https://github.com/Margaritats8/python_labsMT/blob/main/img/lab5/json_csv.png)

### 2. CSV -> JSON
![вывод 2](https://github.com/Margaritats8/python_labsMT/blob/main/img/lab5/csv_json.png)

### 3. CSV -> XLSX
![вывод 3](https://github.com/Margaritats8/python_labsMT/blob/main/img/lab5/lab5_excel.png)

### 4. Пустой JSON файл
![вывод 4](https://github.com/Margaritats8/python_labsMT/blob/main/img/lab5/empty_json.png)

### 5. Битый JSON файл
![вывод 5](https://github.com/Margaritats8/python_labsMT/blob/main/img/lab5/bad_json.png)