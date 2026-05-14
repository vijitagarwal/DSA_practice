MAX=5
cqueue=[None]*MAX
front=-1
rear=-1

def enqueue():
    global front, rear

    if (rear+1)%MAX==front: 
        print("queue overflow")
        return
    
    try:
        element=int(input("enter you want to insert: "))

        if front==-1:   #queue is empty
            front,rear=0
        else:
            rear=(rear+1)*MAX   #normal insertion
        cqueue[rear]=element
        print("element inserted")
    except ValueError:
        print("invalid value")



def dequeue():
    global front,rear
    if front==-1:
        print("queue is empty")
        return
    
    removed=cqueue[front]
    if front==rear: #only one element exists
        front,rear=-1

    else:
        front=(front+1)%MAX
    print(f"element removed {removed}")

def display():
    global front,rear
    if front==-1:
        print("queue is empty")
        return
    i=front
    
    while True:
        print(cqueue[i],end=" ")

        if i == rear:
            break

        i=(i+1)%MAX

    print()


def front_elem():
    if front==-1:
        print("Queue is empty")
        return
    print(f"front element is: {cqueue[front]}")


def rear_elem():
    if rear==-1:
        print("queue is empty")
        return
    print(f"rear element is: {cqueue[rear]}")