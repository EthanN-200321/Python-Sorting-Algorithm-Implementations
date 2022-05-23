def insertionsort(data):
    for i in range(len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and data[j] > temp:
            data[j + 1], data[j] = data[j], data[j + 1]
            j -= 1
            yield data
        data[j + 1], data[data.index(temp)] = data[data.index(temp)], data[j + 1]
        yield data

if __name__ == "__main__":
    a = insertionsort([4, 3, 2, 1])
    for i in a:
        print(i)

