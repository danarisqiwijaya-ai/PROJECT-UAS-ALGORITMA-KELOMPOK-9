Sistem Rekomendasi Handphone (GUI & Struktur Data)

Aplikasi Sistem Rekomendasi Handphone adalah proyek perangkat lunak berbasis Desktop GUI yang dirancang menggunakan library Tkinter. Aplikasi ini berfungsi untuk membantu pengguna dalam mengelola basis data handphone (CRUD), menyaring rekomendasi berdasarkan kriteria budget, membandingkan produk, hingga melacak riwayat navigasi secara dinamis.

Proyek ini dibuat untuk memenuhi syarat Ujian Akhir Praktikum (UAP) Modul Algoritma dan Struktur Data Dasar pada Program Studi S1 Sistem Informasi, Universitas Lampung.

 Anggota Kelompok 9 (Kelas B)
1. Dana Risqi Wijaya
2. Muhammad Hibatullah
3. Pandu Winata
4. Sekar Ayu Maheswari
5. Gita Tri Juliet Marbun


Fitur Utama Aplikasi
Aplikasi ini mengintegrasikan manajemen data internal serta fungsionalitas struktur data tingkat lanjut ke dalam antarmuka yang ramah pengguna:

1. Manajemen Data CRUD Lengkap (In-Memory Database)
   Create:Menambahkan data produk handphone baru ke dalam sistem melalui form input.
     Read: Menampilkan data spesifikasi lengkap secara visual menggunakan komponen ttk.Treeview.
     Update:Memperbarui data spesifikasi, harga, atau rating produk yang dipilih langsung dari tabel.
     Delete: Menghapus produk handphone tertentu dari daftar memori sistem.

2. Sistem Rekomendasi Pintar (Filtering & Ranking)
   Linear Search:Menyaring basis data secara dinamis berdasarkan batas harga maksimum (Max Budget) dan kapasitas RAM minimum.
   Selection Sort: Mengurutkan hasil penyaringan produk secara otomatis dari harga termurah (ascending) untuk mempermudah pengambilan keputusan.

3. Pencarian Instan Tingkat Lanjut (Binary Search Tree - BST)
   Melakukan pencarian data handphone secara cepat berdasarkan nilai kecocokan rating yang tepat (exact rating target) menggunakan struktur pohon biner.

4. Fitur Bandingkan HP (Queue FIFO - Max 3 Produk)
    Memasukkan maksimal 3 produk terpilih ke dalam antrean komparasi menggunakan prinsip First-In, First-Out (FIFO) untuk disandingkan spesifikasinya.

5. Log Navigasi Riwayat Penjelajahan (Doubly Linked List)
    Mencatat jejak digital setiap kali pengguna memilih baris produk pada tabel. Pengguna dapat bergerak maju-mundur melacak produk yang baru saja dilihat menggunakan tombol ◀ Riwayat Sebelumnya dan Riwayat Selanjutnya ▶.

 Implementasi Materi Algoritma & Struktur Data
Sesuai dengan ketentuan regulasi UAP, aplikasi ini dibangun secara murni tanpa menggunakan library eksternal (seperti pandas), melainkan mengimplementasikan 8 cakupan materi utama secara manual:

1. Object-Oriented Programming (OOP): Representasi entitas data smartphone menggunakan class Handphone.
2. Array / List: Memanfaatkan tipe data List bawaan Python sebagai repositori data utama (database_hp).
3. Linear Search: Algoritma pencarian sekuensial untuk menyaring spesifikasi harga dan RAM produk.
4. Selection Sort: Algoritma pengurutan dengan skema pencarian nilai minimum untuk mengurutkan harga termurah.
5. Doubly Linked List: Implementasi mandiri struktur berkait dua arah (DLLNode dengan pointer next dan prev) untuk melacak histori klik pengguna.
6. Queue (Antrean):Penerapan struktur data antrean berbasis array dengan batas kapasitas maksimum 3 produk untuk fitur perbandingan produk.
7. Binary Search Tree (BST): Penyusunan data ke dalam struktur pohon berdasarkan nilai rating untuk mempercepat pencarian data spesifik.
8. Tkinter GUI: Pembangunan antarmuka grafis desktop terstruktur sebagai wadah interaksi pengguna dengan program.
