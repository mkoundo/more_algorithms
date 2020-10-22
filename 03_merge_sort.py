#! python3
# 03_merge_sort.py
# Author: Michael Koundouros
"""
Merge Sort
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm.  Most implementations produce a stable
sort, which means that the order of equal elements is the same in the input and output.
Merge sort is a divide and conquer algorithm.

Conceptually, a merge sort works as follows:

- Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
- Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.
  This will be the sorted list.

worst case performance: O(n log n)
best case performance: O(n log n) typical, O(n) natural variant
average performance: O(n log n)
"""


def merge(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
        merge(L)                # divide left sublist recursively
        merge(R)                # divide right sublist recursively

        # sort left and right arrays
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        # When we run out of elements in either L or R,
        # pick up the remaining elements and put them in the array
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

    return


unsorted = [6, 5, 3, 1, 8, 7, 2, 4]

merge(unsorted)
print(unsorted)
