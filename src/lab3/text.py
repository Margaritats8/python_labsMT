import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    This function brings the text to a standard form.
    What exactly does it do:
      It converts to lowercase (casefold).
      Removes extra spaces and special characters.
      Replaces ё --> e (yo2e).

    Return returns the new text
    '''
    if text == '':
        raise TypeError('Empty string.')
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё','е')
    text = text.replace('\t', ' ').replace('\r', ' ')
    text = text.strip()
    text = ' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    '''
    This function splits the text into words (tokens).

    '''
    if text == '':
        raise TypeError('Empty string.')
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str,int]:
    '''
    This function It counts how many times each 
    unique token is repeated.
    '''
    if len(tokens) == 0:
        raise TypeError('List is empty.')
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str,int], n: int = 5) -> list[tuple[str,int]]:
    top = list(freq.items())
    top.sort(key=lambda x:(-x[1], x[0]))
    return top[:n]

'''
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))'''

test_case1 = count_freq(["a","b","a","c","b","a"])
print(test_case1)
print(top_n(test_case1, n =2))
test_case2 = count_freq(["bb","aa","bb","aa","cc"])
print(test_case2)
print(top_n(test_case2, n = 2))


    
