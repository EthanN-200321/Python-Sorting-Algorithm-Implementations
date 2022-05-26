def _insertionsort(data):
    for i in range(len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and data[j] > temp:
            data[j + 1], data[j] = data[j], data[j + 1]
            j -= 1
        data[j + 1], data[data.index(temp)] = data[data.index(temp)], data[j + 1]
        return data


def bucketsort(data, n):
    buckets = [[] for i in range(n)]
    size = max(data)/len(data)

    for i in range(len(data)):
        j = int (data[i] / size)
        if j != len(data):
            buckets[j].append(data[i])
        else:
            buckets[len(data) - 1].append(data[i])

    for i in range(n):
        buckets[i] = _insertionsort(buckets[i])

    a = []
    for bucket in buckets:
        if bucket:
            a += bucket
    return a

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1, 6]
    n = bucketsort(a, len(a))
    print(n)

