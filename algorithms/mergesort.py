def merge(data, l, mid, h):
    res = []
    i, j = l, mid + 1  # Indices (left, right)
    while i <= mid and j <= h:
        if data[i] < data[j]:
            res.append(data[i])
            i += 1
        else:
            res.append(data[j])
            j += 1
    while i <= mid:
        res.append(data[i])
        i += 1
    while j <= mid:
        res.append(data[j])
        j += 1
    
    for i in range(len(res)):
        data[l+i] = res[i]
        yield data


def mergesort(data, l, h):
    if l >= h:
        return
    
    mid_ind = (l + h) // 2
   
    yield from mergesort(data, l, mid_ind)
    yield from mergesort(data, mid_ind + 1, h)
    yield from merge(data, l, mid_ind, h)

