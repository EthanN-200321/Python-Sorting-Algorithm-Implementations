def selectionsort(data):
    l = len(data)
    for i in range(l):
        mini = i
        for j in range(i + 1, l):
            yield ((data[i], data[mini]), data)
            if data[mini] > data[j]:
                mini = j
        yield ((data[i], data[mini]), data)
        data[i], data[mini] = data[mini], data[i]
        yield ((data[i], data[mini]), data)

if __name__ == "__main__":
    l = [4, 2, 1, 3]
    a = selectionsort(l)
    for i in a:
        print(i)

