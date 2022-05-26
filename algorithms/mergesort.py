def mergesort(data):
    file = open("./outputs/mergesort_output", 'a+')
    file.truncate()
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    l = mergesort(data[mid:])
    r = mergesort(data[:mid])

    res = []
    i, j = 0, 0  # Left index, right index
    while j < len(r) and i < len(l):
        if r[j] > l[i]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
        print((mid, res,(data[mid:], data[:mid])), file=file)
    res.extend(r[j:])
    res.extend(l[i:])
    return res

if __name__ == "__main__":
    a = mergesort([38, 27, 43, 3, 9, 82, 10])
    for i in a:
        print(i)

