1. Deskripsi Project
  
   Project ini merupakan aplikasi backend berbasis Django + Django REST Framework yang digunakan
   untuk mengelola data Produk, Kategori, dan Status Produk (bisa dijual / tidak bisa dijual).
   Aplikasi ini dibuat sebagai bagian dari tes teknis masuk perusahaan,
   Project ini menggunakan framework Django dan menggunakan MySQL sebagai databasenya

2. Teknologi yang Digunakan
   - Python 3.12.0
   - Django 6.0.1
   - MySQL / MariaDB

3. Struktur Database
   ### Buat database dengan nama
   Nama database : fastprint_test_db
   
   ### Tabel kategori
   id_kategori	  | INT (PK)
   nama_kategori	| VARCHAR

   ### Tabel status
   id_status	    | INT (PK)
   nama_status	  | VARCHAR

   ### Tabel produk
   id_produk	    | INT (PK)
   nama_produk	  | VARCHAR
   harga	        | decimal
   kategori_id	  | FK → kategori
   status_id	    | FK → status

4. Setup Project
   ### Git Clone
   https://github.com/Sandyskuy/fastprint_test.git

   ### Virtual Environment
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
   ### Install dependency berikut
   - Django==6.0.1
      ```bash
      pip install django
      ```
   - djangorestframework==3.16.1
      ```bash
      pip install djangorestframework
      ```
   - mysqlclient==2.2.7
     ```bash
     pip install mysqlclient
     ```
   - requests==2.32.5
     ```bash
     python -m pip install requests
     ```
5. Migrasi database
   Project ini menggunakan database yang **sudah tersedia sebelumnya**.

   ⚠️ Catatan penting:
      - Django **tidak membuat database secara otomatis**
      - Database harus dibuat **secara manual**
      - Tabel `produk`, `kategori`, dan `status` dibuat secara manual di MySQL
   
   Migration dijalankan hanya untuk **registrasi struktur tabel ke Django ORM**,
   bukan untuk membuat ulang database atau tabel.

   ### Langkah Migration
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Jalankan server
   ```bash
   python manage.py runserver




