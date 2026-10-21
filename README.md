Markdown<div align="center">

# 🕒 Multi-Token Discord Time Status Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.0%2B-5865F2.svg?logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py)
[![Railway Deploy](https://img.shields.io/badge/Deploy%20on-Railway-0B0D0E.svg?logo=railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Bot Discord asinkron modern untuk mengelola status aktivitas waktu dinamis (WIB) pada multiple bot instance dalam satu proses.*

[Garis Besar](#-garis-besar) • [Fitur Utama](#-fitur-utama) • [Persyaratan](#-persyaratan) • [Panduan Deploy Railway](#-panduan-deploy-247-di-railway) • [Lisensi](#-lisensi)

</div>

---

## 📑 Daftar Isi
- [Garis Besar](#-garis-besar)
- [Fitur Utama](#-fitur-utama)
- [Persyaratan](#-persyaratan)
- [Struktur File](#-struktur-file)
- [Panduan Deploy 24/7 di Railway](#-panduan-deploy-247-di-railway)
  - [1. Hubungkan Repository](#langkah-1-hubungkan-repository-ke-railway)
  - [2. Konfigurasi Environment Variable](#langkah-2-menambahkan-token-di-environment-variables-railway)
  - [3. Verifikasi Log](#langkah-3-deployment--verifikasi)
- [Keamanan](#-keamanan)
- [Lisensi](#-lisensi)

---

## 📌 Garis Besar

**Multi-Token Discord Time Status Bot** adalah solusi ringan berbasis Python untuk menjalankan status jam otomatis di Discord secara *real-time*. Menggunakan `asyncio` dan `discord.py` modern, bot ini mendukung eksekusi **multi-token bersamaan** tanpa memakan banyak konsumsi memori/CPU, menjadikannya sangat ideal dipasang pada cloud platform seperti **Railway**.

---

## ✨ Fitur Utama

- 🤖 **Multi-Bot Instance:** Jalankan beberapa bot Discord sekaligus hanya dengan memisahkan token menggunakan koma (`token1,token2`).
- ⏰ **Dynamic WIB Time Status:** Otomatis memperbarui aktivitas status (*watching status*) setiap jam sesuai Waktu Indonesia Barat (Asia/Jakarta).
- 🎨 **Adaptive Vibes:** Menyesuaikan teks deskripsi berdasarkan jam secara otomatis:
  | Rentang Waktu | Status / Vibes |
  | :--- | :--- |
  | `05:00 - 10:59` | 🌅 **Morning Vibes** |
  | `11:00 - 14:59` | ☀️ **Afternoon Vibes** |
  | `15:00 - 17:59` | 🌇 **Evening Vibes** |
  | `18:00 - 04:59` | 🌌 **Night Vibes** |
- ⚡ **Asynchronous Engine:** Memanfaatkan `discord.ext.tasks` dan `asyncio.gather` untuk performa cepat dan non-blocking.
- 🛡️ **Ultra-Lightweight:** Menggunakan `intents.none()` (hanya `guilds = True`) agar efisien terhadap kuota sumber daya server.

---

## 🛠️ Persyaratan

Pustaka Python yang diperlukan (tercantum dalam `requirements.txt`):

```text
discord.py
pytz
📁 Struktur FilePlaintext.
├── main.py             # Script utama bot Discord
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Dokumentasi proyek
☁️ Panduan Deploy 24/7 di Railway[!NOTE]Railway menyediakan opsi yang sangat stabil untuk menjalankan bot Discord Python 24 jam nonstop tanpa perlu mengurus server VPS sendiri.Langkah 1: Hubungkan Repository ke RailwayAkses Railway Dashboard dan login dengan akun GitHub Anda.Klik tombol New Project $\rightarrow$ pilih Deploy from GitHub repo.Pilih repository bot ini dari daftar repositori Anda.Langkah 2: Menambahkan Token di Environment Variables RailwayDi dalam dashboard service Railway Anda, buka tab Variables.Klik + New Variable dan tambahkan variabel berikut:Key: DISCORD_TOKENValue: Masukkan token bot Discord Anda. Jika menggunakan banyak bot, pisahkan dengan koma , tanpa spasi.[!TIP]Format Value Token:Code snippetNjg5...token1,OTAy...token2,MTAx...token3
Langkah 3: Deployment & VerifikasiRailway akan mendeteksi requirements.txt secara otomatis dan memulai proses build.Buka tab Logs untuk memverifikasi bahwa bot telah berhasil terhubung.Contoh output log sukses:Bash[ONLINE] Bot #1 is logged in as TimeBot#1234
[STATUS - Bot #1] Updated to: Watching Time 14:00 WIB | Afternoon Vibes ☀️
🔒 Keamanan[!WARNING]Jangan pernah memasukkan/menuliskan token Discord secara mentah (hardcode) di dalam berkas kode .py atau mem-push token Anda ke repositori GitHub publik. Gunakan selalu Environment Variable DISCORD_TOKEN.📄 LisensiProyek ini dilindungi di bawah lisensi MIT License. Bebas untuk digunakan, dimodifikasi, dan didistribusikan kembali.
<FollowUp label="Mau saya bantu buatkan template file .gitignore juga agar file sensiti
