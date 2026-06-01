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

    def update(self, id_club, nama_baru, liga_baru, poin_baru):

        current = self.head

        while current:

            if current.data.id == id_club:

                current.data.nama = nama_baru
                current.data.liga = liga_baru
                current.data.poin = poin_baru

                return True

            current = current.next

        return False
           
frame_button = Frame(root, bg="#101820")
frame_button.pack()

Button(
       frame_button,
       text="Tambah Club", 
       width=18, 
       command=tambah_club
).grid(row=0, column=0, padx=5, pady=5)

Button(frame_button, 
       text="Update Club", 
       width=18, 
       command=update_club
).grid(row=0, column=1, padx=5, pady=5)

Button(frame_button,
       text="Hapus Club",
       width=18, 
       command=hapus_club
).grid(row=0, column=2padx=5, pady=5)

Button(frame_button, 
       text="Cari Club",
       width=18, 
       command=cari_data
).grid(row=1, column=0, padx=5, pady=5)

Button(frame_button, 
       text="Urutkan Poin",
       width=18, 
       command=urutkan_poin
).grid(row=1, column=1, padx=5, pady=5)

Button(frame_button, 
       text="Tambah History",
       width=18, 
       command=tambah_history
).grid(row=2, column=0, padx=5, pady=5)

Button(frame_button,
       text="Lihat History",
       width=18,
       command=lihat_history
).grid(row=2, column=1, padx=5, pady=5)

Button(frame_button,
       text="Tambah Watchlist",
       width=18, 
       command=tambah_watchlist
).grid(row=2, column=2, padx=5, pady=5)

Button(frame_button,
       text="Lihat Watchlist",
       width=18, 
       command=lihat_watchlist
).grid(row=3, column=1, padx=5, pady=5)

club1 = Club(1, "Real Madrid", "La Liga", 95)
club2 = Club(2, "Manchester City", "Premier League", 97)
club3 = Club(3, "Barcelona", "La Liga", 90)
club4 = Club(4, "Liverpool", "Premier League", 88)
club5 = Club(5, "Bayern Munich", "Bundesliga", 92)

club_list.tambah(club1)
club_list.tambah(club2)
club_list.tambah(club3)
club_list.tambah(club4)
club_list.tambah(club5)

refresh_data()

root.mainloop()
