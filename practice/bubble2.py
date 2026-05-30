def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
        if not swapped:
            break
    
if __name__=="__main__":
    arr=[1,3,2,5,4]
    bubble_sort(arr)
    print("sorted array")
    print(arr)