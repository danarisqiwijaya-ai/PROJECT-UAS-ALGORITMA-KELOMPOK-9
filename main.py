frame_button = Frame(root, bg="#101820")
frame_button.pack()

Button(frame_button,
       text="Tambah Club", 
       width=18, 
       command=tambah_club
      ).grid(row=0, column=0)
Button(frame_button, 
       text="Update Club", 
       width=18, 
       command=update_club
      ).grid(row=0, column=1)
Button(frame_button,
       text="Hapus Club",
       width=18, 
       command=hapus_club
      ).grid(row=0, column=2)

Button(frame_button, 
       text="Cari Club",
       width=18, 
       command=cari_data
      ).grid(row=1, column=0)
Button(frame_button, 
       text="Urutkan Poin",
       width=18, 
       command=urutkan_poin
      ).grid(row=1, column=1)

Button(frame_button, 
       text="Tambah History",
       width=18, 
       command=tambah_history
      ).grid(row=2, column=0)
Button(frame_button,
       text="Lihat History",
       width=18,
       command=lihat_history
      ).grid(row=2, column=1)

Button(frame_button,
       text="Tambah Watchlist",
       width=18, 
       command=tambah_watchlist
      ).grid(row=2, column=2)
Button(frame_button,
       text="Lihat Watchlist",
       width=18, 
       command=lihat_watchlist
      ).grid(row=3, column=1)

root.mainloop()
