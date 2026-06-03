class DLLNode:
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
        new_node = DLLNode(hp_object)
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

class ComparisonQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if len(self.items) >= 3:
            return False
        self.items.append(item)
        return True

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def get_all(self):
        return self.items

class BSTNode:
    def __init__(self, hp_object):
        self.hp = hp_object
        self.left = None
        self.right = None

class HandphoneBST:
    def __init__(self):
        self.root = None

    def insert(self, hp_object):
        if not self.root:
            self.root = BSTNode(hp_object)
        else:
            self._insert_recursive(self.root, hp_object)

    def _insert_recursive(self, node, hp_object):
        if hp_object.rating < node.hp.rating:
            if not node.left:
                node.left = BSTNode(hp_object)
            else:
                self._insert_recursive(node.left, hp_object)
        else:
            if not node.right:
                node.right = BSTNode(hp_object)
            else:
                self._insert_recursive(node.right, hp_object)

    def search_exact_rating(self, rating_target):
        return self._search_recursive(self.root, rating_target)

    def _search_recursive(self, node, rating_target):
        if not node or node.hp.rating == rating_target:
            return node.hp if node else None
        if rating_target < node.hp.rating:
            return self._search_recursive(node.left, rating_target)
        return self._search_recursive(node.right, rating_target)
