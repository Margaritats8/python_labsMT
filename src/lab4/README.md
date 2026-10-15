# Лаба 4 - Файлы txt/csv и отчёты по текстовой статистике
## Задание A

### read_text

```python
from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Reads and returns the entire content of a text file.

    Defolt text encoding: 'utf-8'. if  you want to change it use:
        read_text("name_of_a_file.txt", encoding="cp1251")
    

    Returns:
        The content of the file as a string.
        If the file was empty it is ok, just returns empty string.
    
    Raises:
        FileNotFoundError: if the file does not exist.
        UnicodeDecodeError if the file cannot be decoded with the specofied encoding.

    '''
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)
```

1. Функция принимает на вход строку или готовый объект Path, после чего приводит аргумент к единому типу Path для дальнейших шагов.
2. С помощью .read_text() осуществляется открытие файла, его декодирование с применением заданной кодировки(по умолчанию utf-8) и загрузка всего содержимого в память в формате единой текстовой строки.
3. Ошибки отсутствия файла FileNotFoundError или несовпадения кодировки UnicodeDecodeError намеренно не перехватываются, позволяя им «всплывать» при вызове скрипта.

### write_csv

``` python 
from pathlib import Path
import csv
from typing import Iterable, Sequence
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    '''
    This function  checks if all rows and the header have the same len.
    If they are correct, it creates the folder (if needed)
    and writes the data to the file.

    Raises:
        ValueError:  if rows or header have different lengths.
    '''
    p = Path(path)
    rows = list(rows)

    if len(rows) > 0:
        dlina = len(rows[0])
        if header is not None:
            rows.append(header)
        for row in rows:
            if len(row) != dlina:
                raise ValueError('Rows have different len')

    
    Path(path).parent.mkdir(parents = True, exist_ok = True)     

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
1. Функция принимает на вход путь к файлу в виде строки или объекта Path. Переданный объект переводится в формат списка списков для фиксации структуры в памяти.

2. Далее идёт проверка на "прямоугольность" и обработка возможной ошибки.

3. Через цепочку вызовов Path(path).parent.mkdir(parents= True, exist_ok=True) функция находит родительский каталог для целевого файла и автоматически создаёт все недостающие промежуточные папки. Последний параметр предотвращает сбой, если директория уже создана.

4. Открывает файл через p.open() в режиме записи с параметром newline="", предотвращающим появление пустых строк на Windows.

5. Инициализирует объект csv.writer(), записывает заголовок (при наличии), после чего в цикле последовательно вносит в файл каждую строку данных.

### Ручные тестики

```python
from src.lab4.io_txt_csv import read_text, write_csv
txt = read_text("src/data/lab4/input.txt") 
print(txt) # должен вернуть строку
write_csv([("word","count"),("test",3)], "src/data/lab4/check.csv")  # создаст CSV
```
Стандартный вывод


![вывод стандарт](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/стандартный_вывод_тест.png)
![вывод стандарт1](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/тест_csv.png)


Нет файла


![нет файла](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/нет_файла.png)


Пустой файл


![пусто](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/пустой_файл.png)

##  Задание В

``` python
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

    file_path = (sys.argv[2] if len(sys.argv)>2 else 'src.data.lab4.input.txt')
    file_enc = (sys.argv[4] if len(sys.argv)>4 else 'utf-8')
    try:
        raw_text = read_text(file_path, encoding = file_enc)
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
```

1. Чтение файла и валидация: Скрипт открывает файл в блоке try-except. Если файла нет (FileNotFoundError), программа выводит ошибку в консоль и останавливает выполнение через return, избегая падения.
2. Далее текст обрабатывается при помощи функций из лабы 3
3. Отсортированный массив all_rows передается в функцию write_csv(), которая записывает его на диск по пути report.csv вместе с заголовком столбцов ("word", "count").
4. В терминал через f-строки выводятся итоговые числовые метрики и список топ-слов в цикле for.(и снова привет от лабы 3)

## Обработка краевых случаев и ошибок

1. Отсутствие входного файла (FileNotFoundError): Если указанный файл по заданному пути не существует, программа прерывает выполнение, выводит в консоль сообщение об ошибке вида `Файл не найден` и завершает работу с кодом.
2. Сбой декодирования (UnicodeDecodeError): Если кодировка файла не соответствует заданной (например, попытка прочесть файл `cp1251` как `utf-8`), программа завершается с уведомлением пользователя о необходимости явного указания параметра `--encoding`.
3. Обработка пустого файла: При передаче пустого файла программа не падает. В консоли выводится статистика о нулевом количестве слов, а в результирующем CSV-файле сохраняется строка заголовка (`word,count`) без контента.

![вывод пусто](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/пустооо.png)
![вывод пусто](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/пуссстоо_csv.png)



4. Большие файлы: ТЗ подразумевает полное считывание файла в оперативную память одной строкой. При обработке очень больших данных в реальных условиях рекомендуется преобразовать логику чтения на построчный вид.
5. Валидация CSV-строк: В модуле io_txt_csv.py находится проверка структуры данных. Если массив содержит строки разной длины, используется исключение ValueError.

## Способ запуска text_report.py

Запуск выполняется из корня репозитория (там, где лежит папка `src/`), с помощью `-m`:

```python
python -m src.lab4.text_report
```

### Базовый тест-кейс

Вход: data/lab4/input.txt
```
Привет, мир! Привет!!!
```
Вывод в консоль терминала:
```
Всего слов: 3
Уникальных слов: 2
Топ-5:
привет: 2
мир: 1
```
Содержимое отчёта data/lab4/report.csv
```
word,count
привет,2
мир,1
```
## Способ запуска cp1251 в text_report.py
Запуск выполняется из корня репозитория (там, где лежит папка `src/`), с помощью `-m`:

```python
python -m src.lab4.text_report --in src/data/lab4/input_cp1251.txt --encoding cp1251
```
![сpp1251](https://github.com/Margaritats8/python_labsMT/blob/main/img/img4/cp1251.png)
