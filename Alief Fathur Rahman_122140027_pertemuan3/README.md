# 💰 Aplikasi Catatan Penabungan Uang

Aplikasi personal dashboard sederhana yang memungkinkan pengguna mencatat aktivitas tabungan harian secara interaktif.  
Pengguna dapat menambahkan, mengedit, dan menghapus data tabungan, lalu menyimpannya ke **localStorage** agar data tidak hilang saat browser ditutup.

---

## ✨ Fitur Aplikasi

- ✅ Tambah data penabungan
- ✅ Edit data yang sudah ditambahkan
- ✅ Hapus data tabungan
- ✅ Total tabungan ditampilkan otomatis
- ✅ Data disimpan ke `localStorage` (persisten)
- ✅ Navigasi dengan **paginasi** (5 entry per halaman)
- ✅ Desain responsif dengan nuansa **kuning cerah**
- ✅ User-friendly dan ringan dijalankan

---

## ⚙️ Fitur ES6+ yang Diimplementasikan

| Fitur ES6+             | Implementasi di Aplikasi                                                           |
|------------------------|------------------------------------------------------------------------------------|
| `let` & `const`        | Digunakan untuk semua deklarasi variabel                                           |
| **Arrow Function**     | ✅ Digunakan di fungsi `render`, `renderPagination`, `updateTotal`, dan lainnya     |
| **Template Literals**  | Digunakan untuk `.innerHTML` saat merender list tabungan                          |
| **Async/Await**        | Dipakai saat menyimpan data edit (simulasi proses asinkron)                        |
| **Class**              | `class Tabungan` digunakan sebagai struktur data tabungan                         |
| **Modules**            | File `main.js` dan `app.js` dipisah menggunakan sintaks `import/export` ES6        |
| **Array Methods**      | Menggunakan `forEach`, `reduce`, `find`, `filter`, `slice`, dan `reverse`         |

---

## 📸 Screenshot Aplikasi
![Hasil Aplikasi]({CA139DD6-E036-4F4C-9EC1-02D44B0E169D}.png)


