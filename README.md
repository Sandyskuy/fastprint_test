1. Deskripsi Project

Project ini merupakan aplikasi backend berbasis Django + Django REST Framework yang digunakan untuk mengelola data Produk, Kategori, dan Status Produk (bisa dijual / tidak bisa dijual).
Aplikasi ini dibuat sebagai bagian dari tes teknis masuk perusahaan, Project ini menggunakan framework Django dan menggunakan MySQL sebagai databasenya

2. Teknologi yang Digunakan
- Python 3.12.0
- Django 6.0.1
- MySQL / MariaDB

3. Struktur Database
Nama database : fastprint_test_db

Tabel kategori
id_kategori	  | INT (PK)
nama_kategori	| VARCHAR

Tabel status 
id_status	    | INT (PK)
nama_status	  | VARCHAR

Tabel produk
id_produk	    | INT (PK)
nama_produk	  | VARCHAR
harga	        | decimal
kategori_id	  | FK → kategori
status_id	    | FK → status

4. Setup Project

