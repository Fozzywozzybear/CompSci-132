'''
CMPSC132 - Quiz 2 Coding Exam
November 19th, 2019
'''

## QUESTION 1

def power(x, n):
    '''
        >>> power(3,4)
        81
        >>> power(4,2)
        16
    '''
    if x==0:#checks to see if it has ran once
        return n
    else:
        return x**power(0,n)







## QUESTION 2

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def __len__(self):
         return len(self.items)


class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> x.dequeue()
        2
        >>> x.enqueue(5)
        >>> x.enqueue(7)
        >>> x.enqueue(-3)
        >>> x.dequeue()
        3
        >>> x
        [5, 7, -3]
    '''
    def __init__(self):
        self.stack_1=Stack()
        self.stack_2=Stack()

    def __str__(self):
        out=self.stack_1.items+self.stack_2.items
        return f'{out}'

    __repr__=__str__

    def isEmpty(self):
        if self.stack_1.isEmpty() and self.stack_2.isEmpty():
            return True
        return False

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        # --YOUR CODE STARTS HERE
        #this code
        if len(self.stack_1)==1:
            value=self.stack_1.items[0]
            self.stack_1.pop()
            return value
        else:
            for i in range(len(self.stack_1)):
                self.stack_2.push(self.stack_1.pop())
            val=self.stack_2.pop()
            for i in range(len(self.stack_2)):
                self.stack_1.push(self.stack_2.pop())
            return val
