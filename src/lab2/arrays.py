def min_max(nums:list[float | int]) -> tuple[float | int, float | int]:
    """
    This function takes list and return min and max of the list.
    
    Input data: list[float | int]

    Raises:
    TypeError('The list should contain only float and int data types.')
        It is necessary to check the data type of the variables inside.

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

#data_cases

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))


def bubble_sort(nums: list[float | int]):  
    """
    Sorting function.

    Input data: list[float | int]

    Example: [1,5,3,2] --> [1,2,3,5]
    """
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
    This function takes list and return sorted list without repeating elements.

    Raises: 
    TypeError('The list should contain only float and int data types.')
        It is necessary to check the data type of the variables inside.
    
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


print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))

def flatten(mat: list[list | tuple]) -> list[float | int]:
    """
    This function takes list, consisting of lists and tuples and returns a list by unpacking
    the contents of the inner elements of the original list.

    Raises:
    TypeError("The list contains elements that are not lists or tuples.")
        It is necessary to check the data type of the variables inside.

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






