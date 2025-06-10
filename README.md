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
