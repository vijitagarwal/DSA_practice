MAX=5
deque=[None]*MAX
front=-1
rear=-1

def is_full():
    return (rear+1)%MAX==front

def is_empty():
    return front==-1

def insert_front():
    global front,rear
    if is_full():
        print("queue is full")
        return
    
    try:
        element=int(input("enter element: "))
        if front==-1:
            front,rear=0
        elif front==0:
            front=MAX-1
        else:
            front-=1
        
        deque[front]=element
        print(f"{element} inserted successfully")

    except ValueError:
        print("invalid value")


def insert_rear():
    global front,rear 
    if is_full():
        print("queue is full")
        return
    
    try:
        element=int(input("Insert value: "))
        if front==-1:
            front,rear=0
        else:
            rear=(rear+1)%MAX

        deque[rear]=element
        print("element inserted successfully",element)
    except ValueError:
        print("invalid value")


def delete_front():
    if is_empty():
        print("queue is empty")

    removed=deque[front]
    if front==rear:
        front,rear=-1
    else:
        front=(front+1)%MAX
    
    print(f"removed {removed}")

def delete_rear():
    if is_empty():
        print("queue is empty")
    
    removed=deque[rear]
    if front==rear:
        front,rear=-1
    elif rear==0:
        rear=MAX-1
    else:
        rear-=1

    print(f"removed {removed}")

def display():

    if is_empty():
        print("queue is empty")
    
    print("printing queue elements")
    i=front
    while True:
        print("queue element are: ",deque[i], end=" ")
        if i==rear:
            break
        i=(i+1)%MAX
    
    print()
