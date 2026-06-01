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

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tampil_semua(self):
        hasil = []
        current = self.head

        while current:
            hasil.append(current.data)
            current = current.next

        return hasil

    def hapus(self, id_club):
        current = self.head
        prev = None

        while current:
            if current.data.id == id_club:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True

            prev = current
            current = current.next

        return False

    def update(self, id_club, nama, liga, poin):
        current = self.head

        while current:
            if current.data.id == id_club:
                current.data.nama = nama
                current.data.liga = liga
                current.data.poin = poin
                return True

            current = current.next

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
