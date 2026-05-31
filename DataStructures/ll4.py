class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedL:
    def __init__(self):
        self.head=None

    
    def insert_beg(self):
        try:
            element=int(input("enter the element you want to insert"))
            new_node=Node(element)
            new_node.next=self.head
            self.head=new_node
            print(f"{element} inserted at the beginning of linked list")
        except ValueError:
            print("invalid input type, enter an integer")
    
    def insert_end(self):
        try:
            element=int(input("enter the element you want to insert at the end: "))
            new_node=Node(element)

            if self.head is None:
                self.head=new_node
                print("element inserted at the end of LL")
                return
            
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            print("element inserted at the end of LL")
        except ValueError:
            print("invalid input type, enter an integer")

    
    def insert_position(self):
        try:
            element=int(input("enter the element you want to insert: "))
            position=int(input("enter the position at which you want the element to be inserted: "))

            if position<=0:
                print("invalid position: indexing starts from one[1]: ")
                return
            
            new_node=Node(element)

            if position==1:
                new_node.next=self.head
                self.head=new_node
                print(f"{element} inserted at {position}")
                return
            
            if self.head is None:
                print("list is empty and you're not inserting at beginning")
                return

            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print("invalid position, list has fewer element")
                    return
                temp=temp.next

            new_node.next=temp.next
            temp.next=new_node
            print(f"{element} inserted at {position}")
        except ValueError:
            print("invalid input type for element or position, try an integer instead")


    def del_beg(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        
        removed=self.head.data
        self.head=self.head.next
        print(f"{removed} is deleted from the beginning of linked list")

    
    def del_end(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return

        if self.head.next is None:
            removed=self.head.data
            self.head=self.head.next
            print(f"{removed} is deleted, list is empty now")
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        removed=temp.next.data
        temp.next=None
        print(f"{removed} is deleted from the end of linked list")

    
    def del_position(self):
        if self.head is None:
            print("list is empty, cannot Delete")
            return
        try:
            position=int(input("enter the position whose element you want to be deleted"))
            
            if position<=0:
                print("invalid position, indexing starts from one[1]")
                return
            
            if position ==1:
                removed=self.head.data
                self.head=self.head.next
                print(f"{removed} is deleted from {position}")
                return
            
            temp=self.head
            for i in range(position-2):
                if temp.next is None:
                    print("Invalid position")
                    return
                temp=temp.next

            if temp.next is None:
                print("invalid position")
                return
            
            removed=temp.next.data
            temp.next=temp.next.next
            print(f"{removed} is deleted from {position}")

        except ValueError:
            print("invalid input type for position, type an integer.")

    
    def display(self):
        if self.head is None:
            print("List is empty, nothing to display")
            return

        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("NULL")

    
    def count(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        print(f"The number of elements in the list is: {count}")


    def search(self):
        if self.head is None:
            print("list is empty, cannot search in an empty list")
            return
        try:
            key=int(input("enter the element you want to look for in the list: "))
            position=1
            temp=self.head

            while temp is not None:
                if key==temp.data:
                    print(f"{key} found at position: {position}")  
                    return
                temp=temp.next
                position+=1

            print(f"{key} not found in list")

        except ValueError:
            print("please enter an integer as key")

    
    def sort(self):
        if self.head is None:
            print("list is empty")
            return
        
        current=self.head
        
        while current is not None:
            index=current.next
            while index is not None:
                if current.data>index.data:
                    current.data,index.data=index.data,current.data
                
                index=index.next
            
            current=current.next
        
        print("list is sorted successfuly")

    def reverse(self):
        prev=None
        current=self.head
        
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        self.head=prev
        print("Linked list is reversed successfully")

if __name__=="__main__":
    ll=LinkedL()
    while True:
        print("Pick a choice from this menu to execute operation on linked list: ")

        print("1. Inserte at beginning of LL")
        print("2. Insert at end of LL")
        print("3. Insert at position in LL")
        print("4. Delete at beginning of LL")
        print("5. Delete at end of LL")
        print("6. Delete at position in LL")
        print("7. Display LL")
        print("8. count the number of elements in LL")
        print("9. Search for a key in LL")
        print("10. Sort")
        print("11. Reverse")
        print("12. Exit the program")

        try: 
            choice=int(input("enter the number corresponding to you choice from the menu: "))

            if choice==1:
                ll.insert_beg()
            
            elif choice==2:
                ll.insert_end()
            
            elif choice==3:
                ll.insert_position()
            
            elif choice==4:
                ll.del_beg()
            
            elif choice ==5:
                ll.del_end()
            
            elif choice==6:
                ll.del_position()
            
            elif choice==7:
                ll.display()

            elif choice==8:
                ll.count()

            elif choice==9:
                ll.search()

            elif choice==10:
                ll.sort()
            
            elif choice==11:
                ll.reverse()
            
            elif choice==12:
                print("program terminated")
                break

            else:
                print("invalid input, chose an option from the menu")
                
        except ValueError:
            print("please enter an integer")
    

                      
