![Screenshot 2025-04-20 233552](https://github.com/user-attachments/assets/8f61f858-8225-404b-ac1b-35d65ed16e30)# Manajemen Buku Pribadi

## Deskripsi Aplikasi
Aplikasi Manajemen Buku Pribadi ini dirancang untuk membantu pengguna dalam mengelola koleksi buku pribadi mereka. Aplikasi ini memungkinkan pengguna untuk:
- Menambahkan buku dengan informasi judul, penulis, dan status buku.
- Mengedit detail buku yang sudah ada.
- Menghapus buku dari daftar.
- Mencari buku berdasarkan judul.
- Memfilter buku berdasarkan status (Milik, Sedang Dibaca, Ingin Dibeli).

Aplikasi ini dibangun menggunakan **React** dan menggunakan **React Context API** untuk pengelolaan status aplikasi, serta **React Router** untuk navigasi antar halaman.

## Instruksi Instalasi dan Menjalankan

1. **Clone Repository**:
   Pertama, clone repository dengan perintah berikut:
   ```bash
   git clone https://github.com/username/book-manager.git
   
Screenshot Antarmuka
Berikut adalah beberapa screenshot antarmuka dari aplikasi yang telah dijalankan.

1. Tampilan Antarmuka Aplikasi
Gambar ini menunjukkan tampilan utama aplikasi di mana pengguna dapat melihat daftar buku yang sudah ditambahkan.
![Screenshot 2025-04-20 233552](https://github.com/user-attachments/assets/d113c053-45bb-4939-862d-f4e9196862f7)

3. Hasil Pengujian Aplikasi
Gambar ini menunjukkan hasil tes yang berhasil dijalankan menggunakan react-testing-library.

4. Hasil Pengujian di Console
Gambar ini menunjukkan hasil tes pada terminal yang menyatakan bahwa sebagian besar tes berhasil dilalui, kecuali satu tes.

Penjelasan Fitur React yang Digunakan
Context API:

Digunakan untuk mengelola status aplikasi secara global, seperti daftar buku. BookContext menyediakan nilai dan fungsi untuk menambah, mengedit, dan menghapus buku, yang bisa diakses oleh komponen lain menggunakan hook useBookContext.

React Router:

Digunakan untuk mengatur navigasi antar halaman di aplikasi. Komponen Routes dan Route memungkinkan aplikasi memiliki beberapa halaman (misalnya, halaman utama dan halaman statistik) tanpa perlu me-reload seluruh aplikasi.

useState dan useEffect:

useState digunakan untuk menyimpan state lokal, seperti status form input (judul, penulis, status). useEffect digunakan untuk mengelola efek samping seperti penghapusan pesan setelah beberapa detik.

useMemo:

Digunakan untuk menghitung statistik buku (total, milik, sedang dibaca, ingin dibeli) hanya ketika data buku berubah, sehingga meningkatkan performa aplikasi.

React Hooks:

Selain useState dan useEffect, useMemo digunakan untuk mengoptimalkan render ulang aplikasi berdasarkan perubahan data.

Komentar dalam Kode untuk Bagian Pentin

Laporan Testing
Aplikasi ini telah diuji menggunakan react-testing-library. Berikut adalah hasil pengujian:
![Testing1](https://github.com/user-attachments/assets/c79fbd23-4a58-44af-a489-9106b8c4a3d9)
![Testing2](https://github.com/user-attachments/assets/54ef3e53-200e-4b24-9bd6-14c111c9ac11)

