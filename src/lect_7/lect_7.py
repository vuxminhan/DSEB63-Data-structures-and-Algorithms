class Node:
    def __init__(self, val, next_node = None):
        self._val = val
        self._next = next_node

class Linked_list:
    def __init__(self):
        self._head = None

    def insert_head(self, val):
        new = Node(val)
        new._next = self._head
        self._head = new

    def insert_middle(self,val, element):
        first = self._head
        new = Node(val)
        while first:
            if first._val == element:
                new._next = first._next
                first._next = new
                self.listprint()
                return
            first = first._next
    def delete_head(self):
        self._head = self._head._next

    def delete_mid(self,element):
        first = Node("",self._head._next)
        self._head = first
        while first:
            try:
                if first._next._val == element:
                    first._next = first._next._next
                    return
                else:
                    first = first._next
            except:
                return
    def listprint(self):
        printval = self._head
        while printval is not None:
            print(printval._val, end = " ")
            printval = printval._next
        print()
    # def remove(self, val):
    #     rmval = Node


list1 = Linked_list()

e2 = "A"
e3 = "B"
e4 = "C"
# Link first Node to second node
list1.insert_head(e2)
list1.insert_head(e3)
list1.insert_middle( e4, "B")
# Link second Node to third node
# e2._next = e3
# list1.delete_head()
list1.delete_mid("B")
list1.listprint()
