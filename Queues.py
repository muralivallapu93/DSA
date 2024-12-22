class Node():
    def __init__(self, value):
        self.value = value
        self.next = Node
class Queues():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    def print_queues(self):
        temp = self.first
        while temp is not None:
            print(temp.next, end=", ")
            temp = temp.next
        print()
    def enqueue(self, value):
        new_node = Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            temp = self.first
            new_node.next = temp
            self.first = temp
        self.length+=1
    def dequeue(self):
        new_node = Node(value)
        if self.length ==0:
            return None
        temp = self.first
        if self.length==1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length-=1
        return temp
            
        



