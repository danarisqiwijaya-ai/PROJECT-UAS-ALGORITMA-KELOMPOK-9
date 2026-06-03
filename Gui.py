import tkinter as tk
from tkinter import messagebox, ttk

from models import Handphone
from algorithms import linear_search_recommendation, selection_sort_by_price
from data_structures import HistoryLinkedList

class RecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rekomendasi HP - Kelompok 5")
        self.root.geometry("800x600")

        self.database_hp = [
            Handphone(1, "Infinix Note 40", 2500000, 8, 256, 4.5),
            Handphone(2, "Samsung Galaxy A55", 5900000, 8, 256, 4.7),
            Handphone(3, "Xiaomi Redmi Note 13", 2300000, 6, 128, 4.3),
            Handphone(4, "iPhone 15 Pro", 19000000, 8, 128, 4.9),
            Handphone(5, "Vivo V30", 4200000, 12, 512, 4.6)
        ]
        self.id_counter = 6
        self.history_log = HistoryLinkedList()

        self.create_widgets()
        self.refresh_table(self.database_hp)

    def create_widgets(self):
        self.lbl_title = tk.Label(self.root, text="Daftar Handphone / Menu Utama CRUD", font=("Arial", 12, "bold"))
        self.lbl_title.pack(pady=5)

        table_frame = tk.Frame(self.root)
        table_frame.pack(padx=15, fill=tk.X)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Nama", "Harga", "RAM", "Storage", "Rating"), show="headings", height=6)
        self.tree.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        for col in ("ID", "Nama", "Harga", "RAM", "Storage", "Rating"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor=tk.CENTER)

  
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        tk.Button(self.root, text="Tampilkan Semua Data", command=lambda: self.refresh_table(self.database_hp), bg="lightgray").pack(pady=3)

        form_frame = tk.LabelFrame(self.root, text=" Form Manipulasi Data HP ", font=("Arial", 10, "bold"))
        form_frame.pack(padx=15, pady=5, fill=tk.X)

        tk.Label(form_frame, text="Nama HP:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ent_nama = tk.Entry(form_frame, width=20)
        self.ent_nama.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Harga (Rp):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.ent_harga = tk.Entry(form_frame, width=20)
        self.ent_harga.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="RAM (GB):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ent_ram = tk.Entry(form_frame, width=20)
        self.ent_ram.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Storage (GB):").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.ent_storage = tk.Entry(form_frame, width=20)
        self.ent_storage.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Rating (0-5):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.ent_rating = tk.Entry(form_frame, width=20)
        self.ent_rating.grid(row=2, column=1, padx=5, pady=5)

     
        crud_btn_frame = tk.Frame(form_frame)
        crud_btn_frame.grid(row=3, column=0, columnspan=4, pady=8)

        tk.Button(crud_btn_frame, text="Tambah HP (Create)", command=self.add_hp, bg="#a3e635", fg="black").pack(side=tk.LEFT, padx=10)
        tk.Button(crud_btn_frame, text="Simpan Perubahan (Update)", command=self.update_hp, bg="#fde047", fg="black").pack(side=tk.LEFT, padx=10)
        tk.Button(crud_btn_frame, text="Hapus HP (Delete)", command=self.delete_hp, bg="#f87171", fg="white").pack(side=tk.LEFT, padx=10)

       
        rec_frame = tk.LabelFrame(self.root, text=" Sistem Rekomendasi Pintar ", font=("Arial", 10, "bold"), fg="blue")
        rec_frame.pack(padx=15, pady=5, fill=tk.X)

        tk.Label(rec_frame, text="Maksimal Budget (Rp):").grid(row=0, column=0, padx=5, pady=8, sticky="e")
        self.ent_budget = tk.Entry(rec_frame, width=15)
        self.ent_budget.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(rec_frame, text="Minimal Kapasitas RAM (GB):").grid(row=0, column=2, padx=5, pady=8, sticky="e")
        self.ent_min_ram = tk.Entry(rec_frame, width=10)
        self.ent_min_ram.grid(row=0, column=3, padx=5, pady=8)

        tk.Button(rec_frame, text="Dapatkan Rekomendasi HP", command=self.get_recommendation, bg="#38bdf8", font=("Arial", 9, "bold")).grid(row=0, column=4, padx=15, pady=8)

        nav_frame = tk.LabelFrame(self.root, text=" Log Riwayat Klik / Penjelajahan (Linked List) ")
        nav_frame.pack(padx=15, pady=5, fill=tk.X)
        
        self.lbl_history = tk.Label(nav_frame, text="Belum ada HP yang dilirik.", font=("Arial", 10, "italic"), fg="gray")
        self.lbl_history.pack(pady=5)
        
        btn_nav_container = tk.Frame(nav_frame)
        btn_nav_container.pack(pady=2)
        tk.Button(btn_nav_container, text="◀ Riwayat Sebelumnya", command=self.prev_history).pack(side=tk.LEFT, padx=20)
        tk.Button(btn_nav_container, text="Riwayat Selanjutnya ▶", command=self.next_history).pack(side=tk.LEFT, padx=20)

   
    def refresh_table(self, data_list):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for hp in data_list:
            self.tree.insert("", tk.END, values=(hp.id, hp.nama, f"Rp{hp.harga:,}", hp.ram, hp.storage, hp.rating))


    def add_hp(self):
        try:
            nama = self.ent_nama.get()
            harga = int(self.ent_harga.get())
            ram = int(self.ent_ram.get())
            storage = int(self.ent_storage.get())
            rating = float(self.ent_rating.get())
            
            if not nama:
                raise ValueError
                
            new_hp = Handphone(self.id_counter, nama, harga, ram, storage, rating)
            self.database_hp.append(new_hp)
            self.id_counter += 1
            self.refresh_table(self.database_hp)
            messagebox.showinfo("Sukses", f"Berhasil menambahkan {nama} ke list!")
        except ValueError:
            messagebox.showerror("Gagal Input", "Pastikan seluruh kolom form terisi dan format data benar!")


    def on_row_select(self, event):
        selected = self.tree.focus()
        if not selected: 
            return
            
        values = self.tree.item(selected, 'values')
        
        self.ent_nama.delete(0, tk.END)
        self.ent_nama.insert(0, values[1])
        self.ent_harga.delete(0, tk.END)
        self.ent_harga.insert(0, values[2].replace("Rp", "").replace(",", ""))
        self.ent_ram.delete(0, tk.END)
        self.ent_ram.insert(0, values[3])
        self.ent_storage.delete(0, tk.END)
        self.ent_storage.insert(0, values[4])
        self.ent_rating.delete(0, tk.END)
        self.ent_rating.insert(0, values[5])

        id_hp = int(values[0])
        for hp in self.database_hp:
            if hp.id == id_hp:
                self.history_log.add_history(hp)
                self.lbl_history.config(text=f"Melihat: {hp.nama} | Harga: Rp{hp.harga:,}", fg="black", font=("Arial", 10, "bold"))
                break


    def update_hp(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Pilih Data", "Silakan klik salah satu baris HP pada tabel terlebih dahulu!")
            return
        
        values = self.tree.item(selected, 'values')
        id_target = int(values[0])

        try:
            for hp in self.database_hp:
                if hp.id == id_target:
                    hp.nama = self.ent_nama.get()
                    hp.harga = int(self.ent_harga.get())
                    hp.ram = int(self.ent_ram.get())
                    hp.storage = int(self.ent_storage.get())
                    hp.rating = float(self.ent_rating.get())
                    break
            self.refresh_table(self.database_hp)
            messagebox.showinfo("Sukses", "Data Handphone berhasil diperbarui!")
        except ValueError:
            messagebox.showerror("Gagal Update", "Format pengisian angka baru salah!")


    def delete_hp(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Pilih Data", "Silakan klik data pada tabel yang ingin dihapus!")
            return
            
        values = self.tree.item(selected, 'values')
        id_target = int(values[0])

        self.database_hp = [hp for hp in self.database_hp if hp.id != id_target]
        self.refresh_table(self.database_hp)
        messagebox.showinfo("Sukses", "Data produk HP berhasil dihapus!")


    def get_recommendation(self):
        try:
            budget = int(self.ent_budget.get())
            min_ram = int(self.ent_min_ram.get())

            filtered_hp = linear_search_recommendation(self.database_hp, budget, min_ram)

            sorted_hp = selection_sort_by_price(filtered_hp, ascending=True)

            if sorted_hp:
                self.refresh_table(sorted_hp)
                messagebox.showinfo("Rekomendasi Berhasil", f"Ditemukan {len(sorted_hp)} HP ideal sesuai kriteria Anda!")
            else:
                messagebox.showinfo("Tidak Cocok", "Tidak ada HP yang sesuai dengan kombinasi budget & RAM tersebut.")
        except ValueError:
            messagebox.showerror("Kriteria Salah", "Tolong isi kriteria budget dan minimal RAM dalam bentuk angka!")


    def prev_history(self):
        hp = self.history_log.get_previous()
        if hp:
            self.lbl_history.config(text=f"Melihat (History): {hp.nama} | Harga: Rp{hp.harga:,}")
        else:
            messagebox.showinfo("Batas Riwayat", "Anda sudah berada pada riwayat klik paling awal.")


    def next_history(self):
        hp = self.history_log.get_next()
        if hp:
            self.lbl_history.config(text=f"Melihat (History): {hp.nama} | Harga: Rp{hp.harga:,}")
        else:
            messagebox.showinfo("Batas Riwayat", "Anda sudah berada pada riwayat klik paling akhir.")
