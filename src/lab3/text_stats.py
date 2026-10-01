from src.lib.text import normalize, tokenize, count_freq, top_n
import sys
raw_text = sys.stdin.read()

clean = normalize(raw_text)
tokens = tokenize(clean)
total_w = len(tokens)
unique = len(set(tokens))
freq_dict = count_freq(tokens)
top_5 = top_n(freq_dict, 5)
print(f'Всего слов: {total_w}')
print(f'Уникальных слов: {unique}')
print('Топ-5:')
for word, count in top_5:
    print(f'{word}:{count}')




