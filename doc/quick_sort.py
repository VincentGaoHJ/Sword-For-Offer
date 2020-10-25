# coding=utf-8
"""
@Time   : 2020/10/24  9:44 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        idx = partition(array, low, high)
        quick_sort(array, low, idx - 1)
        quick_sort(array, idx + 1, high)


if __name__ == '__main__':
    array = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    list_length = len(array)
    quick_sort(array, 0, list_length - 1)

    print(array)
