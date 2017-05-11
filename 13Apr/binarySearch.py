##assuming increasing order sorted list
def binarySearch(arr, l, r, x):
    if (r > l):
        mid = (l + r)/2

        if(x == arr[mid]):
            return mid
        elif x > arr[mid]:
            return binarySearch(arr, mid + 1, r, x)
        else:
            return binarySearch(arr, l, mid - 1, x)
    else:
        return -1

if __name__ == '__main__':
    arr = map(int, raw_input().split(" "))
    x   = input()

    print binarySearch(arr, 0, len(arr), x)

