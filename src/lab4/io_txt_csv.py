from pathlib import Path
import csv
from typing import Iterable, Sequence

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

#добавить мини-тесты и разобрать чё написала хоть

