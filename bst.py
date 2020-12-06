class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

#BinarySearchTree
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    def __str__(self):
        return ("Node({})".format(self.value))
    __repr__=__str__



class BinarySearchTree:
    def __init__(self):
        self.root=None

    def  insert(self,node,value):
        if node is None:
            self.root=Node(value)
        else:
            if value<node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert(node.left,value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert(node.right,value)
    def bfs(self):
        if self.root is None:
            return 'No values in tree'
        q=Queue()
        visited=[]
        q.enqueue(self.root)

        while not q.isEmpty():
            node=q.dequeue()
            visited.append(node.value)

            #left side
            if node.left is not None:
                q.enqueue(node.left)
            #right side
            if node.right is not None:
                q.enqueue(node.right)
        return visited
    def preorder(self,node,visited=None):
        if visited is None:
            visited =[]
        if node is not None:
            visited+=[node.value]
            self.preorder(node.left,visited)
            self.preorder(node.right,visited)
            return  visited
    def inorder(self,node,visited=None):
        if visited is None:
            visited =[]
        if node is not None:
            self.inorder(node.left,visited)
            visited+=[node.value]
            self.inorder(node.right,visited)
            return visited

    def postorder(self,node,visited=None):
        if visited is None:
            visited =[]
        if node is not None:
            self.postorder(node.left,visited)
            self.postorder(node.right,visited)
            visited+=[node.value]
            return visited
