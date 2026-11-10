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

