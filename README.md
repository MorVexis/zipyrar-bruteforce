# 🔐 ZIP & RAR Bruteforce Tool

Sebuah script Python sederhana untuk melakukan bruteforce terhadap file ZIP dan RAR menggunakan wordlist. Tool ini mendukung multi-threading dan menampilkan progress bar saat berjalan.

## 📦 Fitur

- Mendukung file **ZIP** (AES) dan **RAR**
- Menampilkan **progress bar** dengan estimasi waktu
- Mendukung **multi-threading** (dengan `multiprocessing.Pool`)
- Menampilkan total percobaan dan waktu eksekusi

---

## 🛠️ Instalasi

Pastikan Python sudah terinstal. Lalu, install dependency dengan:

```bash
pip install pyzipper rarfile tqdm
