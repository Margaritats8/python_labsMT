# Лаба 3

## Задание А - модуль с функциями 

В переиспользуемом модуле хранятся чистые функции для работы с текстом: нормализация, токенизация, подсчёт частоты и список n топ слов.


### normalize()

Приводит строку к нижнему регистру, также была добавлена проверка на ввод пустой строки, замена ё --> е и удаление спец символов и пробелов.

``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    This function brings the text to a standard form.
    What exactly does it do:
      It converts to lowercase (casefold).
      Removes extra spaces and special characters.
      Replaces ё --> e (yo2e).

    Returns the new text
    '''
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё','е')
    text = text.replace('\t', ' ').replace('\r', ' ')
    text = text.strip()
    text = ' '.join(text.split())
    return text
```

### tokenize()

Текст разбивает на слова, сохраняя дефисы с помощью регулярного выражения r"\w+(?:-\w+)*". Таким образом исключаются знаки препинания, смайлы.

``` python
def tokenize(text: str) -> list[str]:
    '''
    This function splits the text into words (tokens). 
    '''
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens
```

### count_freq() и top_n()

 count_freq подсчитывается частота встретившихся токенов. top_n создаётся топ n токенов(по умолчанию 5), которые встречаются в тексте.

``` python
def count_freq(tokens: list[str]) -> dict[str,int]:
    '''
    This function counts how many times each 
    unique token is repeated.
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str,int], n: int = 5) -> list[tuple[str,int]]:
    '''
    This function finds the most popular words (by default, 5)
    
    Returns a list consisting of tuples that store their
    values and their count.
    '''
    top = list(freq.items())
    top.sort(key=lambda x:(-x[1], x[0]))
    return top[:n]

```
 ### Общий прогон мини-тестов для функций
![Вывод](https://github.com/Margaritats8/python_labsMT/blob/main/img/img3/mini-test.png)



 ## Задание B - text.stats











