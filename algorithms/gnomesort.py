# stupid sort implemented by a stupid person :)
def gnomesort(data):
    i = 0
    while i < len(data):
        yield (data[i], data)
        if i == 0:
            i += 1
        if data[i] >= data[i-1]:
            i += 1
        else:
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1
    yield  (data[i - 1], data)  # (Selected pot, array)

