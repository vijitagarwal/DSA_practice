MAX=5
stack=[0]*MAX
top=-1

def push():
    global top
    if top==MAX-1:
        print("stack is full")
        return
    try:
        element=int(input("enter element you want to push"))
        top+=1
        stack[top]=element
        print(f"{element} pushed into stack")
    except ValueError:
        print("invalid input")

def pop():
    global top
    if top==-1:
        print("Stack is empty")
        return
    removed=stack[top]
    top-=1
    print(f"{removed} removed from stack")

def peek():
    if top==-1:
        print("stack is empty")
        return
    print(f"top element is: {stack[top]}")

def display():
    if top==-1:
        print("stack is empty")
        return
    for i in range(top,-1,-1): #start, stop, step(rangeExcludesStop value)
        print(stack[i])

def search():
    if top==-1:
        print("stack is empty")
        return
    try:
        key=int(input("element you want to search: "))
    except ValueError:
        print("Invalid Input")
        return
    found=False
    for i in range(top,-1,-1):
        if stack[i]==key:
            print("element found at position", top-i+1, "from top")
            found=True
            break
    if not found:
        print("element not found")

def is_Empty():
    if top==-1:
        print("stack is empty")
    else:
        print("stack is not empty")
    
def is_Full():
    if top==MAX-1:
        print("stack is full")
    else:
        print("stack is not full")

def size():
    print("size of stack is: ",top+1)

#MENU DRIVEN CODE
while True:
    print("----stack menu----")
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. Display")
    print("5. Search")
    print("6. isEmpty")
    print("7. isFull")
    print("8. Size")
    print("9. Exit")
    try:
        choice=int(input("enter your choice: "))
        if choice ==1:
            push()
        elif choice ==2:
            pop()
        elif choice ==3:
            peek()
        elif choice==4:
            display()
        elif choice ==5:
            search()
        elif choice ==6:
            is_Empty()
        elif choice ==7:
            is_Full()
        elif choice==8:
            size()
        elif choice ==9:
            print("program terminated")
            break
        else:
            print("invalid choice")
    except ValueError:
        print("please enter a valid integer number")