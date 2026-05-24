def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        # Insert key at correct position
        arr[j + 1] = key


# Driver Code
arr = [12, 11, 13, 5, 6]

insertion_sort(arr)

print("Sorted Array:")
print(arr)