def findNearbyDuplicate(arr, k):
    numSet = {}
    diff = len(arr) + 1

    for i in range(0, len(arr)):
        if numSet.has_key(arr[i]):
            ##matched. there can be multiple matches, hence diff should only store the minimum value.
            if abs(numSet[arr[i]] - i) < diff:
                diff = abs(numSet[arr[i]] - i)
        else:
            numSet[arr[i]] = i

    if diff <= len(arr) and diff <= k:
        return True
    else:
        return False


if __name__ == '__main__':
    arr = map(int, raw_input().split())
    k   = input()

    print findNearbyDuplicate(arr, k)
