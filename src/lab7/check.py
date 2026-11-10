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