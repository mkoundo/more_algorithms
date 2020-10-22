#! python3
# 02_insertion_sort.py
# Author: Michael Koundouros
"""
Insertion Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is
much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However,
insertion sort provides several advantages:
- Simple implementation
- Efficient for (quite) small data sets, much like other quadratic sorting algorithms
- Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(kn) when each
  element in the input is no more than k places away from its sorted position
- Stable; i.e., does not change the relative order of elements with equal keys
- In-place; i.e., only requires a constant amount O(1) of additional memory space
- Online; i.e., can sort a list as it receives it

worst case performance: O(n^2)
best case performance: O(n)
average performance: O(n^2)
"""


def insertion(nums):
    for j in range(1, len(nums)):
        i = j
        while i > 0:
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1
    return


unsorted = [12, 5, 4, 8, 3, 1]

insertion(unsorted)
print(unsorted)
