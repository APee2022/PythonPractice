# traversal a linkedlist
class Node: #create a node
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList: #create a linked list
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def push(self,data):
        new_Node = Node(data)
        new_Node.ref = self.head
        self.head = new_Node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

llist = LinkedList()
llist.push(90)
llist.push(33)
llist.add_end(20)
llist.add_end(13)
llist.add_end(14)
llist.add_end(17)
llist.add_end(21)
llist.add_end(51)
llist.push(99)
llist.add_end(82)
'''
LL1.head = Node(20) #adding data to linked list
l2= Node(40)
l3= Node(80)

LL1.head.ref = l2 #conecting node to each other
l2.ref = l3
'''
llist.print_LL()