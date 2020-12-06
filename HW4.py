#HW4
#Due Date: 12/01/2019, 11:59PM
########################################
#
# Name:Aaron Fosmire
# Collaboration Statement:
#
########################################

class ContentItem():
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class ContentNode():
    def __init__(self, content, nextNode = None):
        self.value = content
        self.next = nextNode

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__

class CacheList():
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))

    __repr__=__str__

    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        new_node=ContentNode(content)
        if new_node.value > self.maxSize:
            return
        if new_node.value > self.remainingSize:
            if evictionPolicy=="lru":
                while new_node.value > self.remainingSize:
                    self.lruEvict()
                #CODE
            elif evictionPolicy=="mru":
                while new_node.value > self.remainingSize:
                    self.mruEvict()
                #CODE
        #inserts to the front
        new_node.next=self.head
        self.head=new_node



    def find(self, cid):
        # YOUR CODE STARTS HERE
        current=self.head
        while current is not None:
    	    if current.cid==cid:
    		    return current
    	    else:
    		    current=current.next
        return None

    def mruEvict(self):
        # YOUR CODE STARTS HERE
        current=self.head
        if self.head==None:
            return
        if current.next==None:
            self.head==None
            self.tail==None
        current=current.next
        return

    def lruEvict(self):
        # YOUR CODE STARTS HERE
        current=self.head
        if self.head==None:#if empty does nothing
            return
        if current.next==None:#if the next value in None set head and tail to none
            self.head=None
            self.tail=None
        prev=current
        while(prev.next.next):#While the next next value of head is real
            prev=prev.next
        prev.next=None #re moves the value
        self.tail=prev

    def clear(self):
        # YOUR CODE STARTS HERE
        current=self.head
        while current.next is not None:
            current=current.next
            self.head=None
            self.tail=None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0
        return 'Cleared cache!'




class Cache():
    """
        >>> cache = Cache()
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
        >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")
        >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
        >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")
        >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
        >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")
        >>> cache.insert(content1, 'lru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> cache.insert(content2, 'lru')
        'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
        >>> cache.insert(content3, 'lru')
        'Insertion not allowed. Content size is too large.'
        >>> cache.insert(content4, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> cache.insert(content5, 'lru')
        'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
        >>> cache.insert(content6, 'lru')
        'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
        >>> cache.insert(content7, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> cache.insert(content8, 'lru')
        "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
        >>> cache.insert(content9, 'lru')
        "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
        >>> cache
        L1 CACHE:
        REMAINING SPACE:177
        ITEMS:2
        LIST:
        [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:45
        ITEMS:1
        LIST:
        [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
        <BLANKLINE>
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:16
        ITEMS:2
        LIST:
        [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
        [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> cache.hierarchy[0].clear()
        'Cleared cache!'
        >>> cache.hierarchy[1].clear()
        'Cleared cache!'
        >>> cache.hierarchy[2].clear()
        'Cleared cache!'
        >>> cache
        L1 CACHE:
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> cache.insert(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> cache.insert(content2, 'mru')
        'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
        >>> cache.retrieveContent(content1)
        CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA
        >>> cache.retrieveContent(content2)
        CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD
        >>> cache.retrieveContent(content3)
        'Cache miss!'
        >>> cache.insert(content5, 'mru')
        'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
        >>> cache.insert(content6, 'mru')
        'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
        >>> cache.insert(content4, 'mru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> cache.insert(content7, 'mru')
        "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> cache.insert(content8, 'mru')
        "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
        >>> cache.insert(content9, 'mru')
        "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
        >>> cache
        L1 CACHE:
        REMAINING SPACE:177
        ITEMS:2
        LIST:
        [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:150
        ITEMS:1
        LIST:
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        <BLANKLINE>
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:12
        ITEMS:2
        LIST:
        [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
        [CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
    """
    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3

    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))

    __repr__=__str__

    def hashFunc(self, contentHeader):
        # YOUR CODE STARTS HERE
        contentHeader=
        level=(sum([ord(c) for c in contentHeader])%self.size)
        return level




    def insert(self, content, evictionPolicy):
        #def put(self, content, evictionPolicy):
        index = self.hashFunc(content.header)
        self.hierarchy[index].put(content,evictionPolicy)
        return 'INSERTED: CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid,self.size,self.header,self.content)


    def retrieveContent(self, content):
        # YOUR CODE STARTS HERE
        level=hashFunc(content)
        if self.hierarchy[self.hashFunc(content)].find( is None:
            return 'Cache miss!'
        else:
            return self.find(level)



        # when the content is not inthe cache
        # >>> cache.retrieveContent(content3)
        # 'Cache miss!'
