#Lab #7
#Due Date: 10/11/2019, 11:59PM 
########################################
#                                      
# Name:Aaron fosmire
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.remDuplicates()
        >>> x.pop()
        8.76
        >>> x
        Head:Node(1)
        Tail:Node(5)
        List:1 3 5
    '''

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count

    def add(self, value):
        if isinstance(value,float) or isinstance(value,int):#checks for float or in
            new_node=Node(value)
            if self.head == None:
                new_node.next=self.head
                self.head=new_node
                self.tail=new_node
            elif self.head.value >= new_node.value:#if the head is > then the new number it puts it in front
                new_node.next=self.head
                self.head=new_node
            else:
                current=self.head # if the other 2 cases are not met then we go through the list  to place items in the right place
                while(current.next != None and current.next.value < new_node.value): # checks for end of list and where to put the new number
                    current=current.next   
                new_node.next=current.next
                current.next=new_node
                self.tail=new_node
        else: 
            return 

    def pop(self):
        current=self.head
        if self.head==None:#if empty does nothing 
            return 
        if current.next==None:#if the next value in None set head and tail to none
            value=current.value
            self.head=None
            self.tail=None
            return value
        prev=current
        while(prev.next.next):#While the next next value of head is real 
            prev=prev.next
        value=prev.next.value
        prev.next=None#re moves the value
        self.tail=prev
        return value

           


    def remDuplicates(self):
        current=self.head
        while current!=None and current.next!=None:#Goes through list till the self.head or self.head.next == None
            if current.value==current.next.value:#Used to replace the value 
                current.next=current.next.next
            else:
                current=current.next
        return 
            
            







