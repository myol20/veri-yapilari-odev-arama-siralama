def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# test
arr = [3, 7, 1, 9, 5]
print(linear_search(arr, 9))
