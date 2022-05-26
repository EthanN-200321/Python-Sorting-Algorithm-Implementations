import random

def bogosort(data):
    def _sorted(data):
        if len(data) < 2:
            return True 
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                return False
        return True

    while not _sorted(data):
        random.shuffle(data)
        yield data
    yield data

