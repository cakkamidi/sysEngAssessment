# Modul Pemesanan Ruangan Odoo

Modul ini berfungsi untuk mengelola master ruangan dan pemesanan ruangan dalam sistem Odoo. Modul ini mencakup:

## Fitur
- **Master Ruangan**: Menyimpan informasi mengenai ruangan seperti nama, tipe, lokasi, kapasitas, dan foto ruangan.
- **Pemesanan Ruangan**: Sistem pemesanan yang mencakup nomor pesanan, pemesan, ruangan, tanggal, dan status pemesanan.
- **Status Pemesanan**: Pemesanan dapat diperbarui dari `Draft` ke `On Going` dan `Done`.
- **Validasi**: 
  - Tidak bisa memesan ruangan yang sudah dipesan pada tanggal yang sama.
  - Nama ruangan dan nama pemesan harus unik.
  
## Instalasi

1. Salin direktori ini ke folder `addons` Odoo Anda.
2. Restart server Odoo Anda.
3. Aktifkan modul melalui menu Aplikasi di Odoo.

## Penggunaan
- **Master Ruangan**: Digunakan untuk membuat dan mengelola data ruangan.
- **Pemesanan Ruangan**: Membuat pemesanan dan mengatur status pemesanan ruangan.

## Validasi
- Nama ruangan dan nama pemesan harus unik.
- Tidak dapat memesan ruangan pada tanggal yang sudah ada pemesanan.