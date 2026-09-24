# Лаба 2


# Задание 1
## Функция mim_max

За мин и макс берем первые элементы списка и дальше проходимся по нему и сравниваем элементы с установленными мин и макс, при необходимости обновляем значения в переменных. На выходе оборачиваем полученные значения в кортеж.

```python
def min_max(nums:list[float | int]) -> tuple[float | int, float | int]:
    """
    This function takes list and return min and max of the list.
    
    Input data: list[float | int]

    Example: [1,2,3] --> (1,3)
    """
    if len(nums) == 0:
        raise ValueError('list is empty')
    minim, maxim = nums[0], nums[0]
    for i in nums:
        if type(i) != int and type(i) != float:
            raise TypeError('The list should contain only float and int data types.')
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
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/min_max.png)


## Функция unique_sorted

Т.к встроенная сортировка запрещена, создаю классическую фукцию пузырьковой сортировки. Короче говоря, прохожусь по списку и меняю элементы местами до тех пор пока все они не будут в правильном порядке. Для проверки уникальности создаю пустой список, прохожусь по исходному и, если в результатном списке нет такого элемента. добавляю элемент.
```Python
def bubble_sort(nums: list[float | int]):  
    '''
    Sorting function.

    Input data: list[float | int]

    Example: [1,5,3,2] --> [1,2,3,5]
    '''
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums
    

def unique_sorted(nums:list[float | int]) -> list[float | int]:
    """
    This function takes list and return sorted list without repeating elements
    
    Example: [3,1,3,2,2,-1] --> [-1,1,2,3]
    """
    res = []
    for i in nums:
        if i not in res:
            if type(i) != int and type(i) != float:
                raise TypeError('The list should contain only float and int data types.')
            else:
                res += [i]
    return bubble_sort(res)

# tets_cases

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
```
Вывод
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/unique_sorted.png)


## Функция flatten

Создаём пустой список и если элемент исходного списка это список или кортеж, то добавляем внутрянку этого элементов в результатный список.
``` python
def flatten(mat: list[list | tuple]) -> list[float | int]:
    """
    This function takes list, consisting of lists and tuples and returns a list by unpacking
    the contents of the inner elements of the original list.

    Example: [[1,2,3],(4,5,5)] --> [1,2,3,4,5,5]
    """
    res = []
    for i in mat:
        if type(i) == list or type(i) == tuple:
            for j in i:
                res += [j]
        else:
            raise TypeError("The list contains elements that are not lists or tuples.")
    return res

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3,4,5)]))
print(flatten([[1], [], [2,3]]))
print(flatten([[1, 2], 'ab']))
```
Вывод 
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/flatten.png)


# Задание 2

## Доп. переиспользуемая функция check_rect

Проверяет матрицы на прямоугольность, чтобы все элеметны были списками и одной длины.
``` python
def check_rect(mat: list[list[float | int]]):
    '''
    This function checking for the matrix to be rectangular.

    Input data: list[list[float | int]]

    Examples: [[1,2,3],[1,2]] --> ValueError
              [[1,2,3], 'ab'] --> TypeError
              [[1,2,3],[4,5,6]] --> True

    '''
    l = len(mat[0])
    for i in mat:
        if len(i) != l:
            raise ValueError("Matrice isn't rectangly.")
        if type(i) != list:
            raise TypeError('The list contains elements that are not lists')
    else:
        return True
```

## Функция transpose

Переворачиваем матрицу. Кол-во новых строк равно кол-ву стобцов, ну а дальше просто заполняем матрицу.
``` python
def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    This function turns matrix m x n --> matrix n x m
    For the operation to be correct, it is necessary to enter a rectangular matrix.

    Example: [[1,2],[3,4]] --> [[1,3],[2,4]]]
    """
    if len(mat) == 0:
        return []
    proverka = check_rect(mat)
    if proverka:
        res = []
        for i in range(len(mat[0])):
            new = []
            for j in range(len(mat)):
                new += [mat[j][i]]
            res.append(new)
        return res

print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2], [3,4]]))
print(transpose([]))
print(transpose([[1,2],[3]]))
```

Вывод:
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/transpose.png)


## Функция row_sums

Тут просто проходимся по строкам матрицы, если она прошла проверку на прямоугольность, и если элементы строк формата int/float, то добавляем их в сумму строки. 
``` python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    This function takes list and return list which contains row sums.

    Input data: list[list[float | int]]

    Example: [[1,2,3],[4,5,6]] --> [6,15]
    """
    res = []
    proverka = check_rect(mat)
    if proverka:
        for stroka in mat:
            res1 = 0
            for i in range(len(stroka)):
                if (type(stroka[i]) != int) and (type(stroka[i]) != float):
                    raise TypeError('The list elements must be lists contains only int/float elemens.')
                else:
                    res1 += stroka[i]
            res += [res1]
    return res

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1,1], [10,-10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1, 2], [3]]))
```

Вывод:
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/row_sums.png)


## Функция col_sums

То же самое, но для столбцов.
``` python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
     This function takes list and return list which contains col sums

     Input data: [list[float | int]]
    
     Example: [[1,2,3],[4,5,6]] --> [5,7,9]
    '''
    res = []     
    proverka = check_rect(mat)
    if proverka:
        for i in range(len(mat[0])):
            res1 = 0
            for j in range(len(mat)):
                if (type(mat[j][i]) != int) and (type(mat[j][i]) != float):
                    raise TypeError('The list elements must be lists contains only int/float elemens.')
                else:
                    res1 += mat[j][i]
            res += [res1]
    return res

print(col_sums([[1, 2,3], [4,5,6]]))
print(col_sums([[-1,1], [10,-10]]))
print(col_sums([[0,0], [0,0]]))
print(col_sums([[1, 2], [3]]))
```

Вывод:
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/col_sums.png)


# Задание 3

## Функция format_record

Беру первый элемент кортежа и спличу его --> избавляюсь от ненужных пробелов, удобно работать. Привожу к нужному формату фамилию, описываю возможные ошибки и добавляю инициалы через цикл. Ну и по красоте через f-строки вывод.
``` python
def format_record(rec: tuple[str, str, float]) -> str:
    """
    This function takes tuple contains (fio, group, GPA) and returns str.

    Input data: tuple[str, str, float]

    Example: ("Иванов Иван Иванович", "BIVT-25", 4.6) --> Иванов И.И., гр. BIVT-25, GPA 4.60
    
    Raises:
    ValueError: Incorrect GPA format.
        When type of GPA isn't float/int or GPA not in 0 < GPA < 5.
    ValueError: Incorrect fio.
        Fio is empty.
    ValueError: Incorrect group.
        Group is empty.
    
    """
    fio = rec[0].split()
    res = fio[0].capitalize() + ' '

    if rec[2] > 5 or rec[2]<0 or (type(rec[2]) != float and type(rec[2]) != int):
        raise ValueError("Incorrect GPA format")
    if fio == []:
        raise ValueError("Incorrect fio.")
    if rec[1] == '':
        raise ValueError("Incorrect group.")
    
    for i in range(1,len(fio)):
        res += (fio[i][0]).upper() + '.'
    res = f'{res}, гр. {rec[1]}, GPA {rec[2]:.2f}'
    return res


print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))
```

Вывод:
![работа функции](https://github.com/Margaritats8/python_labsMT/blob/main/img/img2/format_record.png)


Готово!!!
