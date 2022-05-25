def mergesort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    l = mergesort(data[mid:])
    r = mergesort(data[:mid])

    res = []
    i, j = 0, 0  # Left index, right index
    while j < len(r) and i < len(l):
        if r[j] > l[i]:
            res.append(l[j])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res.extend(r[j:])
    res.extend(l[i:])
    return res

