# Лаба 2


# Задание 1
## Функция mim_max

За мин и макс берем первые элементы списка и дальше проходимся по нему и сравниваем элементы с установленными мин и макс, при необходимости обновляем значения в переменных. На выходе оборачиваем полученные значения в кортеж.

```python
def min_max(nums:list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return 'ValueError'
    minim, maxim = nums[0], nums[0]
    for i in nums:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i
    return (minim, maxim)

#test_cases

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))

```

Вывод




## Функция unique_sorted


Т.к встроенная сортировка запрещена, создаю классическую фукцию пузырьковой сортировки. Короче говоря, прохожусь по списку и меняю элементы местами до тех пор пока все они не будут в правильном порядке. Для проверки уникальности создаю пустой список, прохожусь по исходному и, если в результатном списке нет такого элемента. добавляю элемент.
```Python
def bubble_sort(nums):  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return nums
    

def unique_sorted(nums:list[float | int]) -> list[float | int]:
    res = []
    for i in nums:
        if i not in res:
            res += [i]
    return bubble_sort(res)

# tets_cases

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))


Вывод

## Функция flatten

Создаём пустой список и если элемент исходного списка это список или кортеж, то добавляем внутрянку этого элементов в результатный список.
``` python
def flatten(mat: list[list | tuple]) -> list[float | int]:
    res = []
    for i in mat:
        if type(i) == list or type(i) == tuple:
            for j in i:
                res += [j]
        else:
            return 'TypeError'
    return res


print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3,4,5)]))
print(flatten([[1], [], [2,3]]))
print(flatten([[1, 2], 'ab']))
```


# Задание 2

## Функция transpose

``` python

```

Вывод:


## Функция row_sums

``` python

```

Вывод:

## Функция col_sums

``` python

```

Вывод:


# Задание 3

## Функция format_record

``` python

```

Вывод:
