def bubblesort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            yield data
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    yield data

