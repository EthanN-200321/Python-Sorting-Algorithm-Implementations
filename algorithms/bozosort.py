import random

def bozosort(data):
    def sorted(data):
        if len(data) < 2:
            return True 
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                return False
        return True

    while not sorted(data):
        yield list(data)
        indices = random.sample(range(0, len(data)), k=2)
        data[indices[0]], data[indices[1]], = data[indices[1]], data[indices[0]]
    yield list(data)

