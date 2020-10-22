#! python3
# 05_heap_sort.py
# Author: Michael Koundouros
"""
Heapsort is an in-place sorting algorithm with worst case and average complexity of O(n log n).

The basic idea is to turn the array into a binary heap structure, which has the property that it allows efficient
retrieval and removal of the maximal element. We repeatedly “remove” the maximal element from the heap, thus building
the sorted list from back to front. Heapsort requires random access, so can only be used on an array-like data
structure.

Heapsort is a much more efficient version of selection sort. It also works by determining the largest (or smallest)
element of the list, placing that at the end (or beginning) of the list, then continuing with the rest of the list,
but accomplishes this task efficiently by using a data structure called a heap, a special type of binary tree. Once
the data list has been made into a heap, the root node is guaranteed to be the largest (or smallest) element. When it
is removed and placed at the end of the list, the heap is rearranged so the largest element remaining moves to the
root. Using the heap, finding the next largest element takes O(log n) time, instead of O(n) for a linear scan as in
simple selection sort. This allows Heapsort to run in O(n log n) time, and this is also the worst case complexity.
"""


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heapify(array, end, i):
    left = (2 * i) + 1
    right = (2 * i) + 2
    max = i
    if left < end and array[i] < array[left]:
        max = left
    if right < end and array[max] < array[right]:
        max = right
    if max != i:
        swap(array, i, max)
        heapify(array, end, max)


def heap_sort(array):
    end = len(array)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(array, end, i)
    for i in range(end-1, 0, -1):
        swap(array, i, 0)
        heapify(array, i, 0)


unsorted = [6, 5, 3, 1, 8, 7, 2, 4]

heap_sort(unsorted)

print(unsorted)
