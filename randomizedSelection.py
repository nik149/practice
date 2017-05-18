def RSelect(A, start, end, i):
    if start <= end:
        piv_pos = partition(A, start, end)
        ##we know pivot is in proper place. so now sort only the relevant half of the array and leave the other half as it is.
        if (piv_pos == i):
            return A[piv_pos]
        elif piv_pos > i:
            return RSelect(A, start, piv_pos-1, i)
        else:
            return RSelect(A, piv_pos + 1, end, i)

def partition(A, start, end):
    piv = A[start]
    i = start + 1

    for j in range(start + 1, end + 1):
        if A[j] < piv:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[start], A[i-1] = A[i-1], A[start]

    return i - 1

if __name__ == '__main__':
    arr = map(int, raw_input('Enter array: ').split(" "))
    s = int(raw_input("Enter the order of statistic: "))
    ##s order statistic will be found at s-1 index in the sorted array
    print RSelect(arr, 0, len(arr) - 1, s-1)

