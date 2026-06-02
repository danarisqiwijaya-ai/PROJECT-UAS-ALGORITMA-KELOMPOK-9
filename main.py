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

