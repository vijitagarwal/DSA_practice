def bubbleSort(arr):
    
    n=len(arr)
    for i in range(n):
        swapped=False

        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
            
        if not swapped:
            break

if __name__=="__main__":
    arr=[10,20,4,32,2,13]
    bubbleSort(arr)
    print("sorted array: ")
    print(arr)