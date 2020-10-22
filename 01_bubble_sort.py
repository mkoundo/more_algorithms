#! python3
# 01_bubble_sort.py
# Author: Michael Koundouros
"""
Bubble Sort
This algorithm’s average and worst-case performance is O(n^2), so it is rarely used to sort large, unordered data
sets. Bubble sort can be used to sort a small number of items (where its asymptotic inefficiency is not a high
penalty). Bubble sort can also be used efficiently on a list of any length that is nearly sorted (that is,
the elements are not significantly out of place). For example, if any number of elements are out of place by only one
position (e.g. 0123546789 and 1032547698), bubble sort’s exchange will get them in order on the first pass,
the second pass will find all elements in order, so the sort will take only 2n time.
"""


def bubble(nums):
    check = True
    i = 1
    while check:
        check = False
        for idx in range(len(nums) - i):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                check = True
        i += 1
    return


unsorted = [12, 5, 4, 8, 3, 1]

bubble(unsorted)
print(unsorted)
