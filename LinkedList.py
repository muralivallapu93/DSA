class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value=None):
        if  value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    def print_list(self):
        temp = self.head
        print("print list")
        while temp is not None:
            
            print(temp.value, end=", ")
            temp = temp.next
        print()
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.tail
            # self.tail = new_node
            # temp.next = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return value
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length==0:
            self.head = Node
            self.tail = Node
        return temp.value
    def first_pop(self):
        if self.length ==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length==0:
            self.tail = None
        return temp
    
    def pre_append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return value
    
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index<0 or self.length<=index:
            return None
        if index==0:
            return self.pre_append(value)
        if index==(self.length-1):
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    def remove(self, index):
        if index<0 or self.length<=0:
            return None
        if index==0:
            return self.first_pop()
        if index==(self.length-1):
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before=None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before =temp
            temp = after
        



    
        


obj = LinkedList(1)
for i in range(2,10):
    obj.append(i)
obj.insert(4, 99)
obj.print_list()
obj.reverse()

obj.print_list()

