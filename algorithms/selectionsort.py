def selectionsort(data):
    l = len(data)
    for i in range(l):
        mini = i
        for j in range(i + 1, l):
            yield list(data)
            if data[mini] > data[j]:
                mini = j
        yield list(data)
        data[i], data[mini] = data[mini], data[i]
        yield list(data)

