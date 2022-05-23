import random

def bogosort(data):
    def sorted(data):
        if len(data) < 2:
            return True 
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                return False
        return True

    while not sorted(data):
        random.shuffle(data)
        yield data
    yield data

if __name__ == "__main__":
    a =bogosort([3, 2, 1])
    for i in a:
        print(i)

