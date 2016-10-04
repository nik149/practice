import sys

def mergeSort(arr):
    if(len(arr) == 1):
        return arr

    l = mergeSort(arr[0:len(arr)/2])
    r = mergeSort(arr[len(arr)/2:])

    return merge(l, r)

def merge(a, b):
    mergedArray = []

    while(len(a) & len(b)):
        if(a[0] > b[0]):
            mergedArray.append(b[0])
            del(b[0])
        else:
            mergedArray.append(a[0])
            del(a[0])

    ##For rest of the elements
    while(len(a)):
        mergedArray.append(a[0])
        del(a[0])

    while(len(b)):
        mergedArray.append(b[0])
        del(b[0])

    return mergedArray


if __name__ == '__main__':
    array = map(int, sys.argv[1].split(","))
    sortedArray = mergeSort(array)
    print sortedArray
