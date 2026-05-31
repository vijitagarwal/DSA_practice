arr=[]

#CREATING
def create_arr():
    global arr
    n=int(input("enter number of elements in array:  "))
    arr=[]
    for i in range(n):
        element=int(input(f"enter array element {i+1}: "))
        arr.append(element)
    print("array created successfully")

#DISPLAYING
def display_arr():
    if len(arr)==0:
        print("nothing to display")
        return
    
    print("array element are: ")
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

#INSERTING
def arr_insert():
    pos=int(input("enter position you want to insert at: "))
    if pos<1 or pos>len(arr)+1:
        print("invalid position")
        return
    elm=int(input("enter the element you want to insert: "))
    arr.insert(pos-1,elm)
    print("element inserted successfully")

#DELETING
def arr_delete():
    if len(arr)==0:
        print("array is empty")
        return
    
    pos=int(input("enter position you want to delete at: "))
    if pos<1 or pos>len(arr):
        print("Invalid position")
        return
    
    removed=arr.pop(pos-1)
    print("removed: ",removed)

#SEARCHING
def arr_search():
    if len(arr)==0:
        print("arr is empty")
        return
    
    key=int(input("enter element you want to look for: "))
    found = False
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"key found at position {i+1}")
            found=True
            break
    if not found:
        print("element not found")
    
#UPDATING
def arr_update():
    if len(arr)==0:
        print("array is empty")
        return
    
    pos=int(input("enter position you want to update: "))
    if pos<1 or pos>len(arr):
        print("invalid position")
        return

    new_value=int(input("enter the updated value you want: "))
    arr[pos-1]=new_value
    print("value updated")

#REVERSING
def reverse_arr():
    if len(arr)==0:
        print("empty array")
        return
    
    left=0
    right=len(arr)-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]

        left+=1
        right-=1

    print("arr is reveresed")


#BUBBLE SORT (SORTING)
def sort_arr():
    n=len(arr)
    if n==0:
        print("array is empty")
        return
    
    for i in range(n):
        swapped=False

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    print("array is sorted")


# MENU DRIVEN CODE
while True: 
    print("--------CHOICE MENU--------")
    print("1. Create Array")
    print("2. Display Array")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Update Element")
    print("7. Reverse Array")
    print("8. Sort Array")
    print("9. Exit")
    choice=int(input("enter choice: "))

    if choice == 1:
        create_arr()
    elif choice == 2:
        display_arr()
    elif choice == 3:
        arr_insert()
    elif choice == 4:
        arr_delete()
    elif choice ==5:
        arr_search()
    elif choice == 6:
        arr_update()
    elif choice == 7:
        reverse_arr()
    elif choice ==8:
        sort_arr()
    elif choice==9:
        print("program terminated")
        break
    else:
        print("invalid choice")

