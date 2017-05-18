def quickSort(A, start, end):
    n = len(A)

    if start < end:

        pivot_pos = partition(A, start, end)

        quickSort(A, start, pivot_pos - 1)
        quickSort(A, pivot_pos+1, end)

def partition(A, start, end):
    pivot = A[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[start], A[i-1] = A[i-1], A[start]

    return i-1

if __name__ == '__main__':
    arr = map(int, raw_input().split(" "))
    quickSort(arr, 0, len(arr) - 1)
    print arr
