# ЛР7 - Поиск, сортировка и измерение времени
### Задание А

### search.py
``` python

def linear_search(nums, x):
    """Индекс первого вхождения x или -1.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target): 
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    """То же, что two_sum_brute, но за один проход со словарём."""
    seen = {}  # value -> index
    for j in range(len(nums)):
        need = target - nums[j]
        if need in seen:
            return (seen[need], j)
        seen[nums[j]] = j
    return None



```
1. linear_search: идём по списку одним циклом for, сравнивая каждый элемент с искомым. Как только нашли совпадение — возвращаем его индекс; если цикл закончился, а совпадения не было, возвращаем -1. Сложность 
 
2. binary_search: держим текущие границы в lo и hi и крутим while lo <= hi, каждый раз беря середину mid. Если mid-элемент меньше искомого — сдвигаем левую границу (lo = mid + 1), если больше — правую (hi = mid - 1). Как только lo > hi, значит элемента нет, возвращаем -1. Работает только на отсортированном списке; на неотсортированном результат не определён (об этом сказано в docstring). Сложность

3. two_sum_brute: перебираем все пары индексов (i, j) при i < j двумя вложенными циклами. Сложность O(n²).

4. two_sum_fast: за один проход ведём словарь seen вида «значение → индекс». Для каждого nums[j] смотрим, лежит ли в seen число target - nums[j]; поиск по словарю — O(1), так что весь алгоритм O(n).

### Задание В

### sorting.py
``` python 
def bubble_sort(nums: list[float | int]):  
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums1 = nums[::]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums1) - 1):
            if nums1[i] > nums1[i + 1]:
                nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
                swapped = True
    return nums1

def insertion_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    nums1 = nums[::]
    for i in range(1, len(nums1)):
        current = nums1[i]
        j = i - 1
        while j >= 0 and nums1[j] > current:
            nums1[j + 1] = nums1[j]
            j -= 1
        nums1[j + 1] = current
    return nums1

def selection_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    nums1 = nums[::]
    for i in range(len(nums1) - 1):
        min_index = i
        for j in range(i + 1, len(nums1)):
            if nums1[j] < nums1[min_index]:
                min_index = j
        nums1[i], nums1[min_index] = nums1[min_index], nums1[i]
    return nums1

```
Сортируется копия (nums[::]) и исходный список остаётся нетронутым.

1. bubble_sort: за каждый проход идём по соседним парам и меняем их местами, если они стоят не по порядку, — так элементы по-тихоньку встают на свои места. Флаг swapped останавливает цикл, когда за целый проход не было ни одного обмена, значит список уже упорядочен и менять уже не надо.

2. insertion_sort: берём крайний в неотсортированной части элемент current и двигаем его влево, пока слева стоят большие элементы, — после этого он встаёт на своё место.

3. selection_sort: на каждом шаге в ещё не отсортированной части вручную находим индекс минимального элемента и ставим его на текущую позицию.

Пустой список и список из одного элемента обрабатываются корректно: циклы в них просто не выполняются.


### Задание С

### check.py

``` python
import random

from src.lab7.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab7.sorting import bubble_sort, insertion_sort, selection_sort

checks = 0  # counter of completed checks


def check_sorting(fn, trials=100):
    """Сравнивает fn(nums) со sorted(nums) на случайных списках."""
    global checks
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} didn't work correctly on {original}: {result}" 
        assert nums == original, f"{fn.__name__} modefied the original list: {original}"
        checks += 1


def check_search():
    """linear_search против list.index, binary_search на отсортированных списках."""
    global checks
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-20, 20) for _ in range(n)]
        x = random.randint(-25, 25)

        # linear_search: the index of the first matching element, or -1
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        assert linear_search(nums, x) == expected, f"linear_search didn't work correctly on {nums}, x={x}"
        checks += 1

        # binary_search: on a sorted list
        sorted_nums = sorted(nums)
        i = binary_search(sorted_nums, x)
        if x in sorted_nums:
            assert i != -1 and sorted_nums[i] == x, f"binary_search didn't find {x} in {sorted_nums}"
        else:
            assert i == -1, f"binary_search found a non-existence value {x} in {sorted_nums}" 
        checks += 1

        # checking the end elements
        if sorted_nums:
            for edge in (sorted_nums[0], sorted_nums[-1]):
                i = binary_search(sorted_nums, edge)
                assert i != -1 and sorted_nums[i] == edge, f"binary_search didn't find first or last element {edge} в {sorted_nums}"
                checks += 1


def check_two_sum(trials=100):
    """Оба two_sum дают пару с нужной суммой или оба None."""
    global checks
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)
        assert (a is None) == (b is None), f"two_sum returned different valuues for the list {nums}, target={target}: {a} и {b}"
        for pair in (a, b):
            if pair is not None:
                i, j = pair
                assert i < j and nums[i] + nums[j] == target, f"wrong pair {pair} on {nums}, target={target}"
        checks += 1


def main():
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print(f"OK: {checks} checks.")


if __name__ == "__main__":
    main()

```
1. check_sorting: генерируется 100 случайных списков длиной от 0 до 50, значения от -100 до 100 — с повторами и отрицательными. Каждый результат сверяется с sorted(nums), плюс проверяется, что исходный список не изменился. При расхождении assert выводит список на котором случилось расхождение.

2. check_search: результат linear_search сравнивается с list.index (только -1 вместо ValueError). 

3. binary_search проводится на отсортированных списках: если x найден, происходит проверка sorted_nums[i] == x, если нет — ожидается -1. Крайние элементы проверяются отдельно.

4. check_two_sum: обе программы должны дать одинаковый ответ — либо None, либо пару i < j с нужной суммой target.

Счётчик checks: прибавляется после каждой удачной проверки. В конце вывод OK: N проверок. 
random.seed(42) делает прогон воспроизводимым.

### Задание D

### bench.py

```python
 
import random
import timeit

from src.lab4.io_txt_csv import write_csv
from src.lab7.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab7.sorting import bubble_sort, insertion_sort, selection_sort

LIMIT_N = 10_000  # we don't run quadratic-time sorting algorithms for larger values of n


def make_data(n):
    """Случайный список из n чисел (seed задан один раз в main)."""
    return [random.randint(0, 10 * n) for _ in range(n)]


def bench_sorts(n):
    data = make_data(n)
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    for name, fn in (("bubble", bubble_sort), ("insertion", insertion_sort), ("selection", selection_sort)):
        if n > LIMIT_N:
            rows.append(("sort", n, name, "> 60 с"))  # too long
        else:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, t))
    return rows


def bench_search(n=100_000, queries=10_000):
    data = make_data(n)
    xs = [random.choice(data) for _ in range(queries)]  # the goal is on the list
    rows = []

    def run_linear():
        for x in xs:
            linear_search(data, x)

    t_lin = timeit.timeit(run_linear, number=1)
    rows.append(("search", n, "linear", t_lin))

    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)

    def run_binary():
        for x in xs:
            binary_search(sorted_data, x)

    t_bin = timeit.timeit(run_binary, number=1)
    rows.append(("search", n, "binary", t_bin))
    rows.append(("search", n, "sorted_for_binary", t_sort))
    rows.append(("search", n, "binary+sort", t_bin + t_sort))
    return rows


def bench_two_sum(n):
    # a wide range of values, so that no two pairs have the same sum.
    data = [random.randint(0, 10**12) for _ in range(n)]
    target = data[-2] + data[-1]  #the pair definately exists (at the end of the list)
    rows = []
    t = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("two_sum", n, "brute", t))
    t = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
    rows.append(("two_sum", n, "fast", t))
    return rows


def print_table(rows):
    print(f"{'task':<10} | {'n':>8} | {'impl':<18} | {'seconds':>10}")
    print("-" * 50)
    for task, n, impl, sec in rows:
        if isinstance(sec, float):
            sec = f"{sec:.6f}"
        print(f"{task:<10} | {n:>8} | {impl:<18} | {sec:>10}")


def main():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows += bench_sorts(n)
    rows += bench_search()
    for n in (1_000, 10_000):
        rows += bench_two_sum(n)

    print_table(rows)
    csv_rows = []
    for task, n, impl, sec in rows:
        if isinstance(sec, float):
            sec = f"{sec:.6f}"
        csv_rows.append((task, n, impl, sec))
    write_csv(csv_rows, "data/lab7/bench.csv", header=("task", "n", "impl", "seconds"))


if __name__ == "__main__":
    main()
```

Замер сортировок через timeit.timeit(..., number=1) встроенный sorted и три своих сортировки при разных n. Квадратичные на n = 100 000 не прогоняем — в таблице ставим > 60 с (по теории это ~10¹⁰ шагов).

Замер поисков 10 000 случайных запросов (значения берём из самого списка) к списку на 100 000 элементов. У бинарного поиска сортировка и сам поиск замеряются отдельно, а строка binary+sort показывает суммарное время, чтоб уменьшить погрешность.

Two Sum: за target берем пару последних элементов -- пара точно есть и находится в конце списка = худший случай. Значения берём из диапазона до 10¹², чтобы похожих пар почти не встречалось и перебор прошёл почти все пары.

random.seed(42) ставится ровно один раз — в main. Поэтому внутри одного замера все алгоритмы получают один и тот же список data.

Вывод: таблица создаётся с помощью f-строк, выводится в консоль и сохраняется в data/lab7/benchmark.csv через write_csv.


## Результат работы check.py

Вызов
```
python -m src.lab7.check

```
![](images/lab07/)

---

## Результат бенчмарка

Таблица из `data/lab7/bench.csv` (время в секундах, `random.seed(42)`):

```
task,n,impl,seconds
sort,1000,sorted,0.000170
sort,1000,bubble,0.088767
sort,1000,insertion,0.050307
sort,1000,selection,0.042396
sort,10000,sorted,0.002585
sort,10000,bubble,11.229788
sort,10000,insertion,4.666113
sort,10000,selection,3.888326
sort,100000,sorted,0.035394
sort,100000,bubble,> 60 с
sort,100000,insertion,> 60 с
sort,100000,selection,> 60 с
search,100000,linear,34.399756
search,100000,binary,0.044271
search,100000,sorted_for_binary,0.029511
search,100000,binary+sort,0.073782
two_sum,1000,brute,0.072951
two_sum,1000,fast,0.000366
two_sum,10000,brute,7.468968
two_sum,10000,fast,0.003619
```

![](images/lab07/bench.png)

---

