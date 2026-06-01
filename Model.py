class Club:
    def __init__(self, id_club, nama, liga, poin):
        self.id = id_club
        self.nama = nama
        self.liga = liga
        self.poin = poin

    def tampil(self):
        return f"{self.id} | {self.nama} | {self.liga} | {self.poin}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def tampil(self):
        hasil = []
        cur = self.head
        while cur:
            hasil.append(cur.data)
            cur = cur.next
        return hasil


class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def tampil(self):
        return self.data


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def tampil(self):
        return self.data
