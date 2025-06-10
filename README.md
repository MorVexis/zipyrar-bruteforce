# 🔐 ZIP & RAR Brute Force Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

Tool sederhana namun powerful untuk melakukan **brute-force password** terhadap file **.zip** dan **.rar** menggunakan wordlist. Cocok untuk keperluan **CTF**, **pengujian keamanan**, atau sekadar **pemulihan file pribadi yang lupa password**.

---

## ✨ Fitur

- ✅ Dukungan untuk file **ZIP** dan **RAR**
- 🚀 Proses paralel menggunakan **multiprocessing**
- 📊 Tampilkan progress bar dengan estimasi waktu (`tqdm`)
- ⏱️ Hitung total waktu eksekusi dan jumlah percobaan
- 💥 Otomatis berhenti saat password ditemukan

---

## 🧑‍💻 Dependencies

Pastikan kamu telah menginstal Python 3.8+ dan module berikut:

```bash
pip install pyzipper rarfile tqdm multiprocess
```

---

## ⚙️ Cara Penggunaan

Format Perintah:

```bash
python bruteforce.py -f <file.zip/rar> -w <wordlist.txt> -t <jumlah_threads>
```

Parameter:
```bash
Argumen	Keterangan
-f / --file	File target (ZIP atau RAR)
-w / --wordlist	File wordlist password
-t / --threads	(Opsional) Jumlah thread (default: 2)
```
---

### 📦 Contoh Lengkap

Brute Force ZIP File :

```bash
python bruteforce.py -f dokumen.zip -w wordlist.txt -t 4
```

Brute Force RAR File :

```bash
python bruteforce.py -f arsip.rar -w rockyou.txt -t 6
```

---

### 📤 Contoh Output

Jika password berhasil ditemukan:

```bash
Brute Force Progress: 100%|████████████████████████| 5120/5120 [00:10<00:00, 502.01pass/s]

========================================
[✓] ZIP: Password ditemukan: password123
Total Attempt : 134 Percobaan
[⏱️] Waktu eksekusi: 5.21 detik
========================================
```

Jika password tidak ditemukan:

```bash
[✗] RAR: Password tidak ditemukan.
```

Jika file tidak didukung:

```bash
[!] Format file tidak didukung. Gunakan .zip atau .rar
```

---

### 🗂️ Struktur Proyek

```bash
.
├── bruteforce.py     # Main script
├── wordlist.txt      # Contoh wordlist
├── dokumen.zip       # Contoh file zip
```

---

### ⚠️ Disclaimer
Tool ini hanya untuk tujuan edukasi dan pengujian keamanan terhadap sistem milik sendiri.
Segala bentuk penyalahgunaan merupakan tanggung jawab pengguna.


