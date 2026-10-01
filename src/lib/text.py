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
    # if text == '':
        # raise TypeError('Empty string.')
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
    # if text == '':
        # raise TypeError('Empty string.')
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str,int]:
    '''
    This function It counts how many times each 
    unique token is repeated.
    '''
    # if len(tokens) == 0:
        # raise TypeError('List is empty.')
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str,int], n: int = 5) -> list[tuple[str,int]]:
    top = list(freq.items())
    top.sort(key=lambda x:(-x[1], x[0]))
    return top[:n]
