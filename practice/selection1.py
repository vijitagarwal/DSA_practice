def SelectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

if __name__=="__main__":
    arr=[1,3,2,5,4]
    SelectionSort(arr)
    print("the sorted array using selection sort")
    print(arr)