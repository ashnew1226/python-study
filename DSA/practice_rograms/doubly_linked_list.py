class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="--> ")
                n = n.nref
    def print_LL_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end="--> ")
                n = n.pref
    def insert_empty(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else: 
            print(" Linked list is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    def add_after(self,data,x):
        if self.head is None:
            print("DLL is empty!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:apt list --upgradable
                    break
                n = n.nref           
            if n is None:
                print(f"the given node {x} is not present")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
        
    def add_before(self,data,x):
        if self.head is None:
            print(" DLL is empty!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print(f"the given node {x} is not present")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
    def delete_begin(self):
        if self.head is None:
            print("DDL is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after delete")
        else:
            self.head = self.head.nref
            self.head.pref = None 
    def delete_end(self):
        if self.head is None:
            print("DLL is empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:               # check is it is empty
            print("DLL is empty!")
            return
        if self.head.nref is None:
            if x == self.head.data:           # check if only one node is present
                self.head = None
            else:
                print("given node is not present in DLL")
            return
        if self.head.data == x:             # check if it is first node
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:           # check for middle node 
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:               # delete middle node
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:                  # check for last node and delete
                n.pref.nref = None
            else:
                print(f"{x} is not present in DLL")
dl1 = DoublyLL()
dl1.add_begin(10)
dl1.add_after(40,10)
dl1.add_before(100,10)
dl1.delete_by_value(103)
dl1.print_LL()
dl1.print_LL_reverse()