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
