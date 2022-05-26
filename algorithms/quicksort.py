class QS:
    def __init__(self, data, l, h):  # Run quicksort, store output for visualization in a file
        self.output_file = open("./outputs/quicksort_output", 'a+')
        self.output_file.truncate()

        self._quicksort(data, l, h)
        self.output_file.close()
        

    def _partition(self, data, l, h):
        pivot = data[(h + l) // 2]
        i = l
        j = h


        while True:
            print((pivot, data), file=self.output_file)
            while data[i] < pivot:
                i += 1
            while data[j] > pivot:
                j -= 1
            if i >= j:
                return j
            data[i], data[j] = data[j], data[i]


    def _quicksort(self, data, l, h):
        if l < h:
            pivotind = self._partition(data, l, h)
            self._quicksort(data, l, pivotind)
            self._quicksort(data, pivotind + 1, h)

if __name__ == "__main__":
    a = [6, 1, 2, 3, 4, 9, 8, 0, 7, 5]
    QS(data=a, l=0, h=len(a) - 1)
    

