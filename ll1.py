class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    def insert_beg(self):
        element=int(input("enter element you want to insert at beginning: "))
        new_node=Node(element)

        if self.head is None:
            self.head=new_node
            print(f"new element: {element} inserted into empty LL")
            return
        
        new_node.next=self.head
        self.head=new_node
        print(f"new element: {element} inserted at beginning of LL")


    def insert_end(self):
        element=int(input("enter element you want to insert"))
        new_node=Node(element)

        if self.head is None:
            self.head=new_node
            print(f"new element: {element} inserted into element LL")
            return
        
        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        print(f"element: {element} inserted at the end of LL")

    
    def insert_pos(self):
        element=int(input("enter element you want to insert"))
        position=int(input("enter the position at which you want to insert"))
        new_node=Node(element)

        temp=self.head
        for i in range(position-2):
            temp=temp.next
            if temp is None:
                print("invalid position, can't insert")
                return

        new_node.next=temp.next
        temp.next=new_node
        print(f"element: {element} inserted at position: {position}")


    def del_beg(self):
        if self.head is None:
            print("The LL is empty, cannot delete")
            return
        
        removed=self.head
        if self.head.next is None:
            self.head=None
            print(f"deleted: {removed}, LL is empty now")
        else:
            self.head=self.head.next
            print(f"deleted: {removed}, first element")

    def del_end(self):
        if self.head is None:
            print("The LL is empty, cannot delete")
            return
        
        removed=self.head
        if self.head.next is None:
            self.head=None
            print(f"removed {removed} from LL, list is empty now")
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next

        removed=temp.next.data
        temp.next=None
        print(f"removed: {removed} from the end of linked list")

        
    def del_pos(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        position=int(input("enter the position at which you want to delete"))

        if position==1: #position is one
            removed=self.head.data
            self.head=self.head.next
            print(f"deleted {removed} from {position}")
            return
        
        temp=self.head
        for i in range(position-2):        
            if temp.next==None:
                print(f"Invalid position {position}, Cannot delete")
                return

            temp=temp.next

        if temp.next is None:
            print(f"invalid position {position}, cannot delete")
            return
        
        removed=temp.next.data
        temp.next=temp.next.next
        
        print(f"removed {removed} from position {position}")

    

