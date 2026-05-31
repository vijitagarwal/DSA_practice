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


    def search(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        try: 
            key=int(input("enter the key you want to search for: "))
            temp=self.head
            position=1

            while temp is not None:
                if temp.data==key:
                    print(f"{key} found at position: {position}")
                    return
                
                temp=temp.next
                position+=1

            print("element not found")
        except ValueError:
            print("invalid input type to search for Node")

    
    def count(self):
        count=0
        temp=self.head

        while temp is not None:
            count+=1
            temp=temp.next

        print(f"total number of node is {count}")


    def display(self):
        if self.head is None:
            print("list is empty")
            return

        temp=self.head
        print("Linked list elements are")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("NULL")


## Driver  Code
if __name__ == "__main__":
    ll=LL()

    while True:
        print("\n\n")
        print("Linked list menu")
        print("1 - Insert At Beginning")
        print("2 - Insert at End")
        print("3 - Insert at Position")
        print("4 - Delete at Beginning")
        print("5 - Delete at End")
        print("6 - Delete at Position")
        print("7 - Search in List")
        print("8 - Count number of Nodes")
        print("9 - Display Linked List")
        print("10 - Exit Menu")

        try:
            choice=int(input("Enter your Choice: "))

            if choice==1:
                ll.insert_beg()
            elif choice==2:
                ll.insert_end()
            elif choice==3:
                ll.insert_position()
            elif choice==4:
                ll.del_beginning()
            elif choice==5:
                ll.del_end()
            elif choice==6:
                ll.del_position()
            elif choice==7:
                ll.search()
            elif choice==8:
                ll.count()
            elif choice==9:
                ll.display()
            elif choice==10:
                print("program terminated")
                break
            else:
                print("invalid choice")
        
        except ValueError:
            print("wrong input type for choice")