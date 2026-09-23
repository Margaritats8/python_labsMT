# Лаба 2
№

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