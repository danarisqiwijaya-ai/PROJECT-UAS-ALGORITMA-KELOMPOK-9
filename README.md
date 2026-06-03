Sistem Rekomendasi Handphone 

Aplikasi Sistem Rekomendasi Handphone adalah proyek perangkat lunak berbasis Desktop GUI (tkinter) yang dirancang untuk membantu pengguna menyaring, mengurutkan, dan menemukan perangkat hanphone ideal sesuai anggaran (budget) dan kebutuhan kapasitas RAM tertentu. 

Proyek ini dibuat untuk memenuhi syarat Ujian Akhir Praktikum (UAP) Modul Algoritma dan Struktur Data Dasar pada Program Studi S1 Sistem Informasi, Universitas Lampung.

Anggota Kelompok 9 (Kelas B)
1. Dana Risqi Wijaya
2. Muhammad Hibatullah
3. Pandu Winata
4. Sekar Ayu Maheswari
5. Gita Tri Juliet Marbun

Fitur Utama Aplikasi
Aplikasi ini menggabungkan pengelolaan data internal dan sistem kecerdasan rekomendasi produk dengan fungsionalitas utama sebagai berikut:

1. Sistem Rekomendasi Pintar (Searching & Sorting): Filtering (Linear Search): Menyaring basis data secara dinamis berdasarkan batas harga maksimum dan kapasitas RAM minimum yang diinginkan pengguna.
   
2. Ranking (Selection Sort): Mengurutkan hasil penyaringan produk secara otomatis berdasarkan harga termurah (ascending) guna mempermudah keputusan pembelian.

3. Manajemen Data CRUD Lengkap:
   Create: Admin/User dapat menambahkan data produk Handphone baru lengkap dengan spesifikasi teknisnya.
   Read: Menampilkan visualisasi data berupa tabel interaktif menggunakan komponen ttk.Treeview.
   Update: Memperbarui data spesifikasi atau harga smartphone yang sudah terdaftar secara langsung dari GUI.
   Delete: Menghapus produk smartphone dari basis data memori.
   
4. Log Navigasi Riwayat Penjelajahan (Double Linked List):
   Mencatat jejak digital setiap kali pengguna mengeklik baris produk tertentu di tabel. Pengguna dapat melacak kembali produk apa saja yang baru dilihatnya menggunakan fitur tombol ◀ Riwayat Sebelumnya` dan `Riwayat Selanjutnya ▶.

---

Implementasi Materi Algoritma & Struktur Data
Sesuai dengan ketentuan regulasi UAP, aplikasi ini dibangun secara murni tanpa menggunakan external libraries data science (seperti pandas atau scikit-learn), melainkan mengimplementasikan 6 materi utama secara manual:

1. Object-Oriented Programming (OOP): Penggunaan struktur class dan pembentukan object Handphone sebagai blueprint representasi data entitas.
2. Array / List (Collection): Memanfaatkan tipe data List bawaan Python sebagai wadah penyimpanan koleksi data utama (in-memory database).
3. Double Linked List (Struktur Data Berkait Dua Arah): Pembuatan struktur berkait secara manual (Node, head, tail, next, prev) untuk menggerakkan pointer riwayat penjelajahan produk.
4. Linear Search (Searching): Algoritma pencarian sekuensial langkah demi langkah untuk menyaring kriteria spesifikasi HP.
5. Selection Sort (Sorting): Algoritma pengurutan data dengan skema mencari nilai ekstrem terkecil untuk menukar posisi elemen harga secara efisien.
6. Tkinter UI (Graphical User Interface): Pembangunan antarmuka grafis ramah pengguna (user-friendly) sebagai wadah interaksi aplikasi.

