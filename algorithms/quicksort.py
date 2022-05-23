import random

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[j], data[i] = data[i], data[j]
        data[i+1], data[high] = data[high], data[i+1]
        return i+1


def quicksort(data, low, high):
    if low < high:
        pind = partition(data, low, high)
        quicksort(data, low, pind - 1)
        quicksort(data, pind + 1, high)

if __name__ == "__main__":
    data = [4, 2, 7, 3, 1, 9, 6, 0, 8]
    low, high = 0, len(data)-1
    print("BEFORE SORTING:", data)
    quicksort(data, low, high)
    print("AFTER SORTING:", data)

