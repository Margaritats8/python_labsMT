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