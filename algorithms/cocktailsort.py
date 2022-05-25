def cocktailsort(data):
    swp = True
    end = len(data) - 1
    start = 0

    while swp:  # Loop until no swaps occur
        swp = False
        for i in range(start, end):  # Forward Iteration
            yield data
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swp = True
        
        if swp == False:  # Break if no swaps occur
            break

        for i in range(end-1, start-1, -1):  # Backward iteration
            yield data
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swp = True
        start += 1

