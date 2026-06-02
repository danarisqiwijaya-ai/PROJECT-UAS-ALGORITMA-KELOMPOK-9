class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def hapus(self, id_club):
        cur = self.head
        prev = None

        while cur:
            if cur.data.get_id() == id_club:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next

                return True

            prev = cur
            cur = cur.next

        return False

    def update(self, id_club, nama, liga, poin):
        cur = self.head

        while cur:
            if cur.data.get_id() == id_club:
                cur.data.set_data(nama, liga, poin)
                return True

            cur = cur.next

        return False

    def tampil_semua(self):
        hasil = []

        cur = self.head

        while cur:
            hasil.append(cur.data)
            cur = cur.next

        return hasil


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()

    def tampil(self):
        return self.data


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)

    def tampil(self):
        return self.data


class TreeNode:
    def __init__(self, club):
        self.club = club
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, club):

        def _insert(node, club):

            if node is None:
                return TreeNode(club)

            if club.get_poin() < node.club.get_poin():
                node.left = _insert(node.left, club)
            else:
                node.right = _insert(node.right, club)

            return node

        self.root = _insert(self.root, club)

    def inorder(self):

        hasil = []

        def _in(node):
            if node:
                _in(node.left)
                hasil.append(node.club)
                _in(node.right)

        _in(self.root)

        return hasil[::-1]
