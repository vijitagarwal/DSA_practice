MAX=5
queue=[0]*MAX
front=-1
rear=-1

def enqueue():
    global rear,front
    if rear==MAX-1:
        print("queue is full")
        return
    try:
        element=int(input("enter the element you want to insert: "))
        if front==-1:
            front=0
        rear+=1
        queue[rear]=element
        print("element added to queue")
    except ValueError:
        print("invalid input")
    
    


def dequeue():
    global front,rear
    if front==-1 or front>rear:
        print("queue is empty, cannot dequeue")
        return
    
    removed=queue[front]
    front+=1
    
    if front>rear:
        front=rear=-1
    print("first element from queue removed")


def display():
    if front==-1 or front>rear:
        print("queue is empty")
        return
    for i in range(front,rear+1,1):
        print(queue[i],end=" ")
    print()


def front_elem():
    if front==-1 or front>rear:
        print("queue is empty")
        return
    print(f"the front element is: {queue[front]}")


def rear_elem():
    if front==-1 or front>rear:
        print("queue is empty")
        return
    print(f"print the last element is: {queue[rear]}")


def search():
    if front==-1 or front>rear:
        print("queue is empty")
        return
    try:
        key=int(input("enter the element you want to search: "))
        found=False
        for i in range(front,rear+1,1):
            if key==queue[i]:
                print(f"element found at position {i-front+1}")
                found=True
                break
        if not found:
            print("element not found")
    except ValueError:
        print("invalid input")
        

def size():
    print(f"length of queue is {rear-front+1}")