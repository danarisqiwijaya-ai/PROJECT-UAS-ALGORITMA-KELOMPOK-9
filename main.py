from tkinter import *
from data import club_list, history_stack, watchlist_queue
from model import Club
from logic import cari_club, bubble_sort, binary_search

root = Tk()
root.title("Football Recommendation System")
root.geometry("900x650")
root.configure(bg="#101820")

listbox = Listbox(root, width=100)
listbox.pack(pady=20)


def refresh():
    listbox.delete(0, END)
    for c in club_list.tampil_semua():
        listbox.insert(END, c.tampil())


def tambah():
    c = Club(
        int(entry_id.get()),
        entry_nama.get(),
        entry_liga.get(),
        int(entry_poin.get())
    )
    club_list.tambah(c)
    refresh()


def hapus():
    club_list.hapus(int(entry_id.get()))
    refresh()


def update():
    club_list.update(
        int(entry_id.get()),
        entry_nama.get(),
        entry_liga.get(),
        int(entry_poin.get())
    )
    refresh()


def cari():
    hasil = cari_club(club_list.tampil_semua(), entry_nama.get())

    listbox.delete(0, END)

    for c in hasil:
        listbox.insert(END, c.tampil())


def top3():
    data = bubble_sort(club_list.tampil_semua())[:3]

    listbox.delete(0, END)
    for c in data:
        listbox.insert(END, c.tampil())
frame = Frame(root, bg="#101820")
frame.pack()

Label(frame, text="ID").grid(row=0, column=0)
entry_id = Entry(frame)
entry_id.grid(row=0, column=1)

Label(frame, text="Nama").grid(row=1, column=0)
entry_nama = Entry(frame)
entry_nama.grid(row=1, column=1)

Label(frame, text="Liga").grid(row=2, column=0)
entry_liga = Entry(frame)
entry_liga.grid(row=2, column=1)

Label(frame, text="Poin").grid(row=3, column=0)
entry_poin = Entry(frame)
entry_poin.grid(row=3, column=1)

Button(frame, text="Tambah", command=tambah).grid(row=0, column=2)
Button(frame, text="Update", command=update).grid(row=1, column=2)
Button(frame, text="Hapus", command=hapus).grid(row=2, column=2)
Button(frame, text="Cari", command=cari).grid(row=3, column=2)
Button(frame, text="Top 3", command=top3).grid(row=4, column=2)

club_list.tambah(Club(1, "Real Madrid", "La Liga", 95))
club_list.tambah(Club(2, "Man City", "EPL", 97))
club_list.tambah(Club(3, "Barcelona", "La Liga", 90))

refresh()
root.mainloop()
