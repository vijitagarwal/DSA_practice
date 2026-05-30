def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

if __name__ =="__main__":
    arr=[10,30,20,50,40]
    selection_sort(arr)
    print("sorted using selection sort: ")
    print(arr)