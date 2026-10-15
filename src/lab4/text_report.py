from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab4.io_txt_csv import read_text, write_csv

def main():
    '''
    The main function  of the program
    
    It does the following steps:
    1.Reads raw text from a file.
    2 Cleans the text and splits it into words.
    3.Counts how many times each word arrears.
    4.Finds the top 5 most common words.
    5.Saves all results to a CSV file and prints information.'''
    try:
        raw_text = read_text("src/data/lab4/input.txt", encoding="utf-8")
    except FileNotFoundError:
        print("Файл не найден")
        return

    tokens = tokenize(normalize(raw_text))
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)

    rows = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    top5 = top_n(freq, n=5)

    write_csv(rows, "src/data/lab4/report.csv", header=("word", "count"))

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()