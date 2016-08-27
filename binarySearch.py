import sys
##input a sorted array and search item
def binarySearch(arr, l, r, x):
    mid = int((l + r)/2)

    if(r < l):
        return -1

    if(int(arr[mid]) == int(x)):
        return mid

    if(int(arr[mid]) > int(x)):
        return binarySearch(arr, l, mid-1, x)
    else:
        return binarySearch(arr, mid+1, r, x)


if __name__ == '__main__':
    arr = sys.argv[2].split(",")
    x   = sys.argv[1]
    ind = binarySearch(arr, 0, len(arr) - 1, x)
    print ind
