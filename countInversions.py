##counts number of pairs of array indices (i,j)
##such that A[i] > A[j] where i<j
def countInv(arr):
    if len(arr) == 1:
        return arr, 0

    n     = len(arr)

    left, lc  = countInv(arr[0:n/2])
    right, rc = countInv(arr[n/2:])
    merged, sc = countSplitInv(left, right)

    return merged, lc + rc + sc

def countSplitInv(a,b):
    i = 0
    j = 0
    count = 0
    n = len(a)
    c = []
    while(len(a) and len(b)):
        if a[i] > b[j]:
            c.append(b[0])
            del(b[0])
            #since array is sorted, all elements after i in a will also be > than b[j]. hence increase count by all remaining elements in a
            count += (len(a))
        else:
            c.append(a[i])
            del(a[0])

    while len(a):
        c.append(a[0])
        del(a[0])

    while len(b):
        c.append(b[j])
        del(b[0])

    return c, count



if __name__ == '__main__':
    arr =  [int(line.rstrip('\n')) for line in open('input.txt')]
    #arr = map(int, raw_input("Enter array values").split(" "))
    c, cnt = countInv(arr)
    print cnt
