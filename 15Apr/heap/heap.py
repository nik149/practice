class Heap:
    def __init__(self, array, heapType):
        self.array = array
        self.count = len(array) - 1
        self.heap_type = heapType   ##heap_type = 1 => max heap. = 2 => min heap

    def getParent(self, i):
        if i <= 0 or i > self.count:
            return -1
        return (i-1)/2

    def leftChild(self, i):
        left = 2*i + 1
        if left < 0 or left > self.count:
            return -1
        return left

    def rightChild(self, i):
        right = 2*i + 2
        if right < 0 or right > self.count:
            return -1
        return right

    def max_heapify(self, i):
        largest = i ## this should be the case, but since it's not, we're heapifying.
        print "i: ", i

        left = self.leftChild(i)
        right = self.rightChild(i)
        print "children: ", left, right
        if left <= self.count and self.array[left] > self.array[i]:
            largest = left
        elif right <= self.count and self.array[right] > self.array[i]:
            largest = right

        if largest != i :
            print "Swapping"
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.max_heapify(largest)

    ##build max heap from an array
    def build_maxheap(self):
        for i in range(len(self.array)/2, 0, -1):
            self.max_heapify(i)

    def insert(self, data):
        if self.heap_type == 1:
            self.array.append(data)
            self.count += 1
            i = self.count - 1

            ##find the appropriate position
            while i > 0 and data >= self.array[i]:
                self.array[i] = self.array[(i-1)/2]
                i = (i-1)/2
        else:
            ##TODO
            print "Not yet programmed"


if __name__ == '__main__':
    A = map(int, raw_input().split(" "))
    heapType = input("1 for Max Heap, 2 for Min Heap")
    heap = Heap(A, heapType)

    if heapType == 1:
        print "Max heapifying"
        heap.build_maxheap()

    print heap.array



