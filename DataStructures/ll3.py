class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    
    def insert_beginning(self):
        try:
            element=int(input("enter element You want to insert at beginning: "))
            new_node=Node(element)

            new_node.next=self.head
            self.head=new_node
            print(f"{element} inserted at beginning of LL")

        except ValueError:
            print("Invalid element type (enter an integer)")

    
    def insert_end(self):
        try:
            element=int(input("enter the value you want to insert at the end: "))
            new_node=Node(element)

            if self.head is None:
                self.head=new_node
                print(f"{element} inserted at end")
                return
            
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            
            temp.next=new_node
            print(f"{element} inserted at end")

        except ValueError:
            print("Invalid element type (enter an integer)")


    def insert_position(self):
        try:
            element=int(input("enter the element you want to insert: "))
            position=int(input("enter the position at which you want to insert the element "))
            new_node=Node(element)

            if position<=0:
                print("Invalid position, should be greater than zero [0]")
                return
            
            if position ==1:
                new_node.next=self.head
                self.head=new_node
                print(f"{element} inserted at position: {position}")
                return
            
            if self.head is None:
                print("Invalid position, list is empty and you're not inserting at beginning")
                return
                
            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print("Invalid position, list has fewer element than you think")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
            print(f"{element} inserted at position: {position}")

        except ValueError:
            print("Invalid element or position type, only integers accepted")

    
    def delete_beginning(self):
        if self.head is None:
            print("cannot delete, list is empty")
            return
        
        removed=self.head.data
        self.head=self.head.next
        print(f"{removed} is removed from the beginning of the list")

    
    def delete_end(self):
        if self.head is None:
            print("cannot delete, list is empty")
            return
    
        if self.head.next is None:
            removed=self.head.data
            self.head=None
            print(f"{removed} is removed from the end of list, list is empty now")
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        removed=temp.next.data
        temp.next=None
        print(f"{removed} is removed from the end of list")

    
    def delete_position(self):
        if self.head is None:
            print("cannot delete, list is empty")
            return
        
        try:
            position=int(input("enter the position whose element you want to delete: "))

            if position<=0:
                print("Invalid position, should be greater than zero[0]")
                return
            
            if position==1:
                removed=self.head.data
                self.head=self.head.next
                print(f"{removed} is removed from position {position}")
                return

            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print("Invalid position, list has fewer elments than you assumed")
                    return
                temp=temp.next
            if temp.next is None:
                print("Invalid position, reduce the value by atleast 1")
                return
            
            removed=temp.next.data
            temp.next=temp.next.next
            print(f"{removed} is removed from the list which was at {position}")
        
        except ValueError:
            print("Invalid position data type, enter only integer.")


    def display(self):
        if self.head is None:
            print("list is empty, insert something to display")
            return

        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("NULL")

    def search(self):
        if self.head is None:
            print("list is empty, insert something to search")
            return
        
        try:
            key=int(input("enter the key you want to search: "))
            temp=self.head
            position =1

            while temp is not None:
                if key==temp.data:
                    print(f"{key} found at position {position}")
                    return
                temp=temp.next
                position+=1

            print(f"{key} not found in list.")
        
        except ValueError:
            print("invalid key type, only integers can exist is list")

    
    def count(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        print(f"the number of elements in the list is {count}")
    