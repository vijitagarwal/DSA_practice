class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class Doublyll:
    def __init__(self):
        self.head=None


    def insert_beg(self):
        element=int(input("enter element you want to insert: "))
        new_node=Node(element)

        if self.head is None:
            self.head=new_node
            print("element inserted into empty list")
            return
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        print("element inserted at begining")


    def insert_end(self):
        element=int(input("enter element you want to insert: "))
        new_node=Node(element)

        if self.head is None:
            self.head=new_node
            print("element inserted into empty list")
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        print("inserted at end")
    

    def del_beg(self):
        if self.head is None:
            print("list is empty, cannot delete")
            return
        
        removed=self.head.data
        if self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

        print(f"{removed} removed from beginning")


    def del_end(self):
        if self.head is None:
            print("list is empty, cannot delete")
            return

        if self.head.next is None:
            removed=self.head.data
            self.head=None
            print(f"{removed} element removed")
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next

        removed=temp.data
        temp.prev.next=None
        temp.prev=None
        print(f"{removed} element removed from end")


    def display_ascending(self):
        if self.head is None:
            print("list is empty")
            return
        
        temp=self.head
        print("list elements are: ")

        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.next
        print("NULL")
    

    def display_descending(self): 
        if self.head is None:
            print("list is empty")
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next #we are at end now
        
        print("list elements are: ")

        while temp:
            print(temp.data,end=" <-> ") #printing
            temp=temp.prev #moving backward

        print("NULL")