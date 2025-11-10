class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")

    def preorder(self):
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end = " ")

    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:                            # check data is lesser & go to left subtree
            if self.lchild:
                print(f"self.lchild - {self.lchild.key}")
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Given node is not present.")
        elif data > self.key:                           # check data is greater & go to right subtree
            print("inside greater side")
            if self.rchild:
                print(f"self.rchild - {self.rchild.key}")
                self.rchild = self.rchild.delete(data,curr)
                print(f"self.rchild after self.rchild.delete(data) - {self.rchild}")
            else:
                print("Given node is not present")
        else:
            if self.lchild is None:                     # if node has left child
                print("inside l child")
                print(f"self.key - {self.key}")
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None 
                return temp
            if self.rchild is None:                     # if node has right chlid
                print("inside r child")
                print(f"self.key - {self.key}")
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                print(f"temp - {temp.key}")             # return temp to called delete recursion method
                return temp
            node = self.rchild                          # if node is having 2 child nodes
            print(f"node - {node.key}")                     
            while node.lchild:                          # check left child for selected node
                node = node.lchild
            self.key = node.key                         # make left child of node is the current node
            self.rchild = self.rchild.delete(node.key,curr)  # put smallest right child
        return self
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(f"smallest node is : {current.key}")
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(f"largest node is : {current.key}")
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
root = BST(10)
list1 = [1,12]
for i in list1:
    root.insert(i)
# root.search(32)
print("Preorder - ")
root.preorder()
print()
print("min node -")
root.min_node()
root.max_node()
# if count(root) > 1:
#     root.delete(10,root.key)
# else:
    # print("cant perform delete operation.")
print("after delete")
print("Preorder - ")
root.preorder()
print()
