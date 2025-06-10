<h1 align="center">🔐 ZIP & RAR Brute Force Tool</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey" alt="Platform">
</p>


<p align="center">
  Tool sederhana namun powerful untuk melakukan <strong>brute-force password</strong> terhadap file <code>.zip</code> dan <code>.rar</code> menggunakan wordlist.<br>
  Cocok untuk keperluan <strong>CTF</strong>, <strong>pengujian keamanan</strong>, atau sekadar <strong>pemulihan file pribadi yang lupa password</strong>.
</p>


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
python brutezipyrar.py -f <file.zip/rar> -w <wordlist.txt> -t <jumlah_threads>
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
python brutezipyrar.py -f dokumen.zip -w wordlist.txt -t 4
```

Brute Force RAR File :

```bash
python brutezipyrar.py -f arsip.rar -w rockyou.txt -t 6
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
├── brutezipyrar.py     # Main script
├── wordlist.txt      # Contoh wordlist
├── dokumen.zip       # Contoh file zip
```

---

### ⚠️ Disclaimer
Tool ini hanya untuk tujuan edukasi dan pengujian keamanan terhadap sistem milik sendiri.
Segala bentuk penyalahgunaan merupakan tanggung jawab pengguna.


