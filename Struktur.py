class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  

class HistoryLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None  

    def add_history(self, hp_object):
        new_node = Node(hp_object)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.current = self.tail  

    def get_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def get_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None
