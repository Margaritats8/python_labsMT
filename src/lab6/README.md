# ЛР6 - CLI-утилиты с argparse (cat/grep-lite + конвертеры)
### Задание А

### `cli_text.py`

``` python 
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab4.io_txt_csv import read_text


def check_file(path: str) -> None:
    '''Checks that the input file exists.
    '''
    if not Path(path).is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")


def cmd_cat(path: str, numbered: bool) -> None:
    '''Prints the file line by line; with numbered=True — with line numbers.
    '''
    check_file(path)
    text = read_text(path)
    number = 1
    for line in text.splitlines():
        if numbered:
            print(f"{number}. {line}")
        else:
            print(line)
        number += 1


def cmd_stats(path: str, top: int) -> None:
    '''Prints the top-N most frequent words in the file.
    '''
    check_file(path)
    text = read_text(path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Total words: {len(tokens)}")
    print(f"Unique words: {len(freq)}")
    print(f"Top-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-utilities for working with text") # вот отсюда и ниже разобрать код
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Print file contents")
    cat_parser.add_argument("--input", required=True, help="Path to the file")
    cat_parser.add_argument("-n", action="store_true", help="Number the lines")

    stats_parser = subparsers.add_parser("stats", help="Word frequencies in text")
    stats_parser.add_argument("--input", required=True, help="Path to the text file")
    stats_parser.add_argument("--top", type=int, default=5, help="How many words to output (default 5)")

    args = parser.parse_args()

    if args.command is None:
        parser.error("a subcommand must be specified: cat or stats")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("--top must be a positive number")
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
1. check_file проверяет, что по указанному пути лежит существующий файл. Иначе поднимается FileNotFoundError с пояснением.

2. Команда cat: cmd_cat считывает файл с помощью read_text (переиспользуется из ЛР4) и выводит содержимое построчно. Если задан ключ -n, каждая строка сопровождается своим порядковым номером.

3. Команда stats: cmd_stats обрабатывает текст конвейером normalize -> tokenize -> count_freq (переиспользуется из ЛР3), после чего печатает общее количество слов, количество уникальных слов и топ-N наиболее частых слов, получаемый через top_n. Значение --top по умолчанию — 5.

4. В main создаётся ArgumentParser, а с помощью add_subparsers(dest="command") регистрируются подкоманды cat и stats. Для каждой подкоманды объявляется свой набор аргументов: --input, -n, --top.

5. При отсутствии подкоманды либо при значении --top <= 0 срабатывает parser.error(...). Отсутствие файла перехватывается в main через except FileNotFoundError.

### Задание В

### `cli_convert.py`
``` python 
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
```

1. Функции json_to_csv, csv_to_json и csv_to_xlsx подключаются из ЛР5.

2. add_subparsers(dest="cmd") создаёт три подкоманды — json2csv, csv2json и csv2xlsx. У каждой объявлены обязательные аргументы --in и --out. Так как in зарезервирован в Python, значения принимаются в args.input и args.output — переименование выполняется через dest.

3. По значению args.cmd выбирается и вызывается нужная функция из ЛР5. После успешного завершения печатается сообщение вида Готово: файл1 -> файл2

4. FileNotFoundError и ValueError, выбрасываемые функциями ЛР5, обрабатываются в main.

## Способ запуска

Запуск выполняется из корня репозитория.

```
python -m src.lab06.cli_text <команда> [параметры]
python -m src.lab06.cli_convert <команда> [параметры]
```

| Программа | Команда | Параметры |
|---|---|---|
| `cli_text` | `cat` | `--input <путь>` (обязательный), `-n` (нумерация строк) |
| `cli_text` | `stats` | `--input <путь>` (обязательный), `--top <N>` (по умолчанию 5) |
| `cli_convert` | `json2csv` | `--in <файл.json>`, `--out <файл.csv>` |
| `cli_convert` | `csv2json` | `--in <файл.csv>`, `--out <файл.json>` |
| `cli_convert` | `csv2xlsx` | `--in <файл.csv>`, `--out <файл.xlsx>` |

## Тест-кейс А: `cat`

![]

## Тест-кейс B: `stats`
### Входной файл data/lab6/text.txt`:
```
Симба рос на землях прайда и мечтал стать королём. Муфаса учил сына, что король
должен заботиться о землях и о прайде. Шрам завидовал брату и плел интриги.
Однажды Шрам обманул Симбу, и Муфаса погиб. Симба бежал из прайда и долго жил
вдали от дома. Тимон и Пумба научили Симбу жить без забот. Но прошлое звало
Симбу назад. Симба вернулся, победил Шрама и занял своё место на скале прайда.

```
![]

## Тест-кейс C: конвертеры

Запуск
```
python -m src.lab6.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
python -m src.lab6.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
python -m src.lab6.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```
Вывод в консоль:

```
Done : data/samples/... -> data/out/...
```
Результат: в папке `data/out/` созданы файлы people.csv, people.json, people.xlsx.

![]

## Тест-кейс D: ошибки
Файл не найден: python -m src.lab6.cli_text cat --input a.txt

Неверное расширение: python -m src.lab6.cli_convert json2csv --in src/data/samples/people.csv --out x.csv

Неверный аргумент: python -m src.lab6.cli_text stats --input src/data/samples/people.txt --top -5

![]

## Тест-кейс E: --help

```
python -m src.lab6.cli_text --help
```
![]

```
python -m src.lab6.cli_convert --help
```
![]



