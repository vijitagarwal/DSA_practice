class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None


    def insert_end(self):
        element=int(input("enter value: "))
        new_node=Node(element)

        if self.head==None:
            self.head=new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        print(f"{new_node} is added at end")


    def insert_beg(self):
        element=int(input("enter value: "))
        new_node=Node(element)
        
        new_node.next=self.head

        self.head=new_node
        print("new node inserted at beginning")


    def del_beg(self):
        if self.head==None:
            print("list is empty")
            return
        
        removed = self.head.data
        self.head=self.head.next
        print(f"{removed} removed from list")


    def del_end(self):
        if self.head is None:
            print("list is empty")
            return
        
        if self.head.next==None:     #only one element
            removed=self.head.data
            self.head=None
            print(f"deleted node {removed}")
            return

        temp=self.head      #normal case
        while temp.next.next is not None:
            temp=temp.next
            removed=temp.next.data
            temp.next=None
            print(f"removed {removed}") 


    def display(self):
        if self.head is None:
            print("list is empty")
            return
        
        temp=self.head
        print("linked list elements are: ")

        while temp is not None:
            print(temp,end="->")
            temp=temp.next

        print("NULL")

    def search(self):
        if self.head is None:
            print("list is empty")
            return
        
        key=int(input("enter the element you want to find: "))
        position=1
        temp=self.head

        while temp is not None:
            if temp.data ==key:
                print(f"key found at position: {position}")
                return

            temp=temp.next
            position+=1

        print("Element not found!")

ll=linked_list()

while True:
    print("linked list menu")
    print("1. Insert at beginning")


    try:
        choice=int(input("enter your choice"))
        if choice ==1:
            ll.insert_beg()
        
        elif choice ==2:
            ll.insert_end()

        elif choice==3:
            ll.del_beg()
        
        elif choice ==4:
            ll.del_end()
        
        elif choice ==5:
            ll.display()

        elif choice ==6:
            ll.search()

        elif choice ==7:
            print("program terminated")
            break

        else:
            print("invalid choice")

    except ValueError:
        print("invalid input")




