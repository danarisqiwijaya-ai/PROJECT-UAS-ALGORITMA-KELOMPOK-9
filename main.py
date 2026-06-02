from tkinter import *

from model import Club
from structures import BST
from algorithms import *
from data_store import *

root = Tk()

root.title("Football Recommendation System")
root.geometry("1000x750")
root.configure(bg="#101820")

Label(root,
      text="⚽ FOOTBALL RECOMMENDATION SYSTEM",
      bg="#101820",
      fg="white",
      font=("Segoe UI", 22, "bold")).pack(pady=10)

frame_input = Frame(root, bg="#1c2431", padx=10, pady=10)
frame_input.pack(pady=10)

entry_id = Entry(frame_input)
entry_nama = Entry(frame_input)
entry_liga = Entry(frame_input)
entry_poin = Entry(frame_input)

entry_id.grid(row=0, column=1)
entry_nama.grid(row=1, column=1)
entry_liga.grid(row=2, column=1)
entry_poin.grid(row=3, column=1)

Label(frame_input, text="ID", bg="#1c2431", fg="white").grid(row=0, column=0)
Label(frame_input, text="Nama", bg="#1c2431", fg="white").grid(row=1, column=0)
Label(frame_input, text="Liga", bg="#1c2431", fg="white").grid(row=2, column=0)
Label(frame_input, text="Poin", bg="#1c2431", fg="white").grid(row=3, column=0)

frame_list = Frame(root)
frame_list.pack(pady=10)

scroll = Scrollbar(frame_list)
scroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame_list,
                  width=120,
                  height=18,
                  yscrollcommand=scroll.set)

listbox.pack()

scroll.config(command=listbox.yview)


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
    history.push(c)

    tambah_ke_liga(c)

    refresh()


def update():
    club_list.update(
        int(entry_id.get()),
        entry_nama.get(),
        entry_liga.get(),
        int(entry_poin.get())
    )

    refresh()


def hapus():
    club_list.hapus(int(entry_id.get()))
    refresh()


def cari():
    hasil = cari_club(
        club_list.tampil_semua(),
        entry_nama.get()
    )

    listbox.delete(0, END)

    for c in hasil:
        listbox.insert(END, c.tampil())


def sort():
    data = bubble_sort(
        club_list.tampil_semua()
    )

    listbox.delete(0, END)

    for c in data:
        listbox.insert(END, c.tampil())


def bst_rekomendasi():
    bst = BST()

    for c in club_list.tampil_semua():
        bst.insert(c)

    hasil = bst.inorder()

    listbox.delete(0, END)

    listbox.insert(END, "=== REKOMENDASI BST ===")

    for c in hasil[:5]:
        listbox.insert(END, c.tampil())


def lihat_liga():
    listbox.delete(0, END)

    for liga, clubs in liga_map.items():

        listbox.insert(END, f"=== {liga} ===")

        for c in clubs:
            listbox.insert(END, c.tampil())


def history_view():
    listbox.delete(0, END)

    for h in history.tampil():
        listbox.insert(END, h.tampil())


def watchlist_view():
    listbox.delete(0, END)

    for w in watchlist.tampil():
        listbox.insert(END, w.tampil())


frame_btn = Frame(root, bg="#101820")
frame_btn.pack(pady=15)

Button(frame_btn, text="Tambah",
       width=12, bg="#2ecc71",
       command=tambah).grid(row=0, column=0)

Button(frame_btn, text="Update",
       width=12, bg="#f1c40f",
       command=update).grid(row=0, column=1)

Button(frame_btn, text="Hapus",
       width=12, bg="#e74c3c",
       command=hapus).grid(row=0, column=2)

Button(frame_btn, text="Cari",
       width=12, bg="#3498db",
       command=cari).grid(row=1, column=0)

Button(frame_btn, text="Sort",
       width=12, bg="#9b59b6",
       command=sort).grid(row=1, column=1)

Button(frame_btn, text="BST",
       width=12, bg="#1abc9c",
       command=bst_rekomendasi).grid(row=1, column=2)

Button(frame_btn, text="Liga",
       width=12, bg="#16a085",
       command=lihat_liga).grid(row=2, column=0)

Button(frame_btn, text="History",
       width=12, bg="#34495e",
       command=history_view).grid(row=2, column=1)

Button(frame_btn, text="Watchlist",
       width=12, bg="#2c3e50",
       command=watchlist_view).grid(row=2, column=2)

club_list.tambah(Club(1, "Real Madrid", "La Liga", 95))
club_list.tambah(Club(2, "Manchester City", "Premier League", 97))
club_list.tambah(Club(3, "Barcelona", "La Liga", 90))
club_list.tambah(Club(4, "Liverpool", "Premier League", 88))
club_list.tambah(Club(5, "Bayern Munich", "Bundesliga", 92))

for c in club_list.tampil_semua():
    tambah_ke_liga(c)

refresh()
