

def findNearbyDuplicate(arr, k):
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if (arr[i] == arr[j]) and  (abs(i - j)) <= k :
                return True, i, j

    return False

if __name__ == '__main__':
    arr = map(int, raw_input().split(" "))
    k = input()
    print findNearbyDuplicate(arr, k)


