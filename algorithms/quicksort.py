import random
def partition(data, l, h):
    pivot = data[(h + l) // 2]
    i = l
    j = h

    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]


def quicksort(data, l, h):
    if l < h:
        pivotind = partition(data, l, h)
        quicksort(data, l, pivotind)
        quicksort(data, pivotind + 1, h)

