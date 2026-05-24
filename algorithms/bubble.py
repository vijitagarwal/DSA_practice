def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):

        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        # If no swapping happens, array is sorted
        if not swapped:
            break


# Driver Code
arr = [5, 6, 1, 3,10,20,2,-2,-4]

bubble_sort(arr)

print("Sorted Array:")
print(arr)