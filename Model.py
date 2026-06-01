class Club:
    def __init__(self, id_club, nama, liga, poin):
        self.id = id_club
        self.nama = nama
        self.liga = liga
        self.poin = poin

    def tampil(self):
        return f"{self.id} | {self.nama} | {self.liga} | Poin: {self.poin}"


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

    def tampil_semua(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def hapus(self, id_club):
        cur, prev = self.head, None
        while cur:
            if cur.data.id == id_club:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def update(self, id_club, nama, liga, poin):
        cur = self.head
        while cur:
            if cur.data.id == id_club:
                cur.data.nama = nama
                cur.data.liga = liga
                cur.data.poin = poin
                return True
            cur = cur.next
        return False


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def tampil(self):
        return self.data


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def tampil(self):
        return self.data
