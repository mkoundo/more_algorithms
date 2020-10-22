#! python3
# 04_selection_sort.py
# Author: Michael Koundouros
"""
Selection Sort
Selection sort is an in-place comparison sort. It has O(n^2) complexity, making it inefficient on
large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its
simplicity, and also has performance advantages over more complicated algorithms in certain situations. First find
the smallest element in the array and swap it with the element in the first position, then find the second smallest
element and swap it with the element in the second position, and continue in this way until the entire array is
sorted. Its asymptotic complexity is O(n^2) making it inefficient on large arrays. Its primary purpose is for when
writing data is very expensive (slow) when compared to reading, eg. writing to flash memory or EEPROM. No other
sorting algorithm has less data movement. It does no more than n swaps, and thus is useful where swapping is very
expensive.
"""


def selection(nums):
    i = 0
    while i < len(nums):
        for idx in range(i, len(nums)):
            if nums[idx] < nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
        i += 1
    return


unsorted = [6, 5, 3, 1, 8, 7, 2, 4]

selection(unsorted)
print(unsorted)
