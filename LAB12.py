#LAB 12
#Due Date: 11/22/2019, 11:59PM
########################################
#
# Name:
# Collaboration Statement:
#
########################################

class MinHeap:
    ### Copy and paste your code from LAB 9 here
    def __init__(self):
        self.heap=[]


    def __str__(self):
    	return f'{self.heap}'

    __repr__=__str__


    def parent(self,index):
        i=index
        if i <=1  or i>len(self.heap):
            return None
        x=i//2
        if x>=0:
            return self.heap[x-1]
        else:
            return None

    def leftChild(self,index):
        left=2*index
        if left > len(self.heap):
            return None
        return self.heap[left-1]

    def rightChild(self,index):
        right=2*index+1
        if right > len(self.heap):
            return None
        return self.heap[right-1]

    def __len__(self):
        return len(self.heap)

    def insert(self,x):
        self.heap.append(x)
        self.sortUp(x)

    def sortUp(self,x):
        index=self.heap.index(x)
        i=index-1
        parent=i//2
        if parent <0:
            parent=0
        if index==0:
            return
        if self.leftChild(x) is None:
            return
        if self.heap[index]>=self.heap[parent]:
            return
        if self.heap[index]<self.heap[parent]:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self.sortUp(x)
        else:
            return

    def sortDown(self,x):
        y=x-1
        left=2*y+1
        right=2*y+2
        tmp=0

        if self.rightChild(x) == None or self.leftChild(x)==None:
            return
        if self.leftChild(x)>=self.heap[y] and self.rightChild(x)>=self.heap[y]:
            return
        if self.rightChild(x) == None:
            if self.leftChild(x)<self.heap[y]:
                self.heap[y],self.heap[left]=self.heap[left],self.heap[y]
                self.sortDown(left+1)
                return
        if self.rightChild(x)<self.leftChild(x):
            if self.rightChild(x)<=self.heap[y]:
                self.heap[y],self.heap[right]=self.heap[right],self.heap[y]
                self.sortDown(right+1)
                return
        if self.leftChild(x)<self.rightChild(x):
            if self.leftChild(x)<=self.heap[y]:
                self.heap[y],self.heap[left]=self.heap[left],self.heap[y]
                self.sortDown(left+1)
                return


#poopyhead hahahahaha

    @property
    def deleteMin(self):
        if len(self)==0:
            return None
        elif len(self)==1:
            out=self.heap[0]
            self.heap=[]
            return out
        out=self.heap[0]
        self.heap[0]=self.heap[(len(self)-1)]
        self.heap.pop()
        self.sortDown(1)
        return out


def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''

    sort_heap = MinHeap()
    storage=[]
    for i in numList:
        sort_heap.insert(i)
    while len(sort_heap.heap)!=0:
        storage.append(sort_heap.deleteMin)


    return storage
