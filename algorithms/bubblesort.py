def bubblesort(data):
    l = len(data)
    for i in range(l):
        for j in range(l - i - 1):
            yield data
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    yield data


if __name__ == "__main__":
    a = bubblesort([3, 2, 1])
    for i in a:
        print(i)

