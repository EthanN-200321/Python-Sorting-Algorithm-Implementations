def quicksort(data, l, h):
    # Partitioning
    if l < h:
        pivot = data[(h + l) // 2]
        i = l
        j = h


        while True:
            yield list(data)
            while data[i] < pivot:
                i += 1
            while data[j] > pivot:
                j -= 1
            if i >= j:
                pivotind = j
                break
            data[i], data[j] = data[j], data[i]

        yield list(data)
        
        # Quicksort
        yield from quicksort(data, l, pivotind)
        yield from quicksort(data, pivotind + 1, h)

