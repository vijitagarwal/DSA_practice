class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def insert_beg(self):
        try:
            element=int(input("enter the value you want to insert: "))
            new_node=Node(element)

            new_node.next=self.head
            self.head=new_node
            print(f"inserted {element} at the beginning of linked list")
        except ValueError:
            print("Invalid input type")

    
    def insert_end(self):
        try: 
            element=int(input("enter the value you want to insert: "))
            new_node=Node(element)

            if self.head is None:
                self.head=new_node
                print("element inserted at the end of linked list")
                return
            
            temp=self.head
            while temp.next is not None:
                temp=temp.next

            temp.next=new_node
            print(f"{element} inserted at the end of LL")

        except ValueError:
            print("invalid input type")


    def insert_position(self):
        try:
            element=int(input("enter the value you want to insert: "))
            position=int(input("enter the position at which you want to insert: "))

            if position <=0:
                print("invalid position")
                return
            
            new_node=Node(element)
            if position==1:
                new_node.next=self.head
                self.head=new_node
                print(f"{element} insert at {position}")
                return
            
            if self.head is None:
                print("list is empty and you are not inserting at beginning")
                return
            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print("invalid position")
                    return
                temp=temp.next

            new_node.next=temp.next
            temp.next=new_node
            print(f"{element} inserted at {position}")

        except ValueError:
            print("invalid input type")
        


    def del_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        
        removed=self.head.data
        self.head=self.head.next
        print(f"{removed} is removed from linked list")

    
    def del_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next is None:
            removed=self.head.data
            self.head=None
            print(f"{removed} is removed, list is empty now")
            return

        temp=self.head
        while temp.next.next is not None:
            temp=temp.next

        removed=temp.next.data
        temp.next=None
        print(f"{removed} is removed from list")

    
    def del_position(self):
        try: 
            if self.head is None:
                print("list is empty")
                return
            
            position=int(input("enter position at which you want to delete: "))

            if position <=0:
                print(f"invalid position: {position}, count starts from one[1].")
                return
            
            if position==1:
                removed=self.head.data
                self.head=self.head.next
                print(f"{removed} is removed from list")
                return
            
            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print(f"Invalid position {position}")
                    return
                temp=temp.next

            if temp.next is None:
                print(f"Invalid Position {position}")
                return
            
            removed=temp.next.data
            temp.next=temp.next.next
            print(f"{removed} is removed from {position} in the list")

        except ValueError:
            print("invalid input type")

        