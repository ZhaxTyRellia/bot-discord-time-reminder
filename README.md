<div align="center">

# 🕒 Multi-Token Discord Time Status Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.0%2B-5865F2.svg?logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py)
[![Railway Deploy](https://img.shields.io/badge/Deploy%20on-Railway-0B0D0E.svg?logo=railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Bot Discord asinkron modern untuk mengelola status aktivitas waktu dinamis (WIB) pada multiple bot instance dalam satu proses.*

[Garis Besar](#-garis-besar) • [Fitur Utama](#-fitur-utama) • [Persyaratan](#-persyaratan) • [Instalasi Lokal](#-panduan-instalasi-lokal) • [Deploy Railway](#-panduan-deploy-247-di-railway) • [Lisensi](#-lisensi)

</div>

---

## 📑 Daftar Isi
- [Garis Besar](#-garis-besar)
- [Fitur Utama](#-fitur-utama)
- [Persyaratan](#-persyaratan)
- [Struktur File](#-struktur-file)
- [Panduan Instalasi Lokal](#-panduan-instalasi-lokal)
- [Panduan Deploy 24/7 di Railway](#-panduan-deploy-247-di-railway)
  - [1. Hubungkan Repository](#langkah-1-hubungkan-repository-ke-railway)
  - [2. Konfigurasi Environment Variable](#langkah-2-menambahkan-token-di-environment-variables-railway)
  - [3. Verifikasi Log](#langkah-3-deployment--verifikasi)
- [Keamanan](#-keamanan)
- [Lisensi](#-lisensi)

---

## 📌 Garis Besar

**Multi-Token Discord Time Status Bot** adalah solusi ringan berbasis Python untuk menjalankan status jam otomatis di Discord secara *real-time*. Menggunakan `asyncio` dan `discord.py` modern, bot ini mendukung eksekusi **multi-token bersamaan** tanpa memakan banyak konsumsi memori/CPU, menjadikannya sangat ideal dipasang pada cloud platform seperti **Railway** ataupun dijalankan secara lokal.

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

```

---

## 📁 Struktur File

```text
.
├── main.py             # Script utama bot Discord
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Dokumentasi proyek

```

---

## 💻 Panduan Instalasi Lokal

Jika Anda ingin mengunduh dan menguji bot ini di komputer lokal Anda, ikuti langkah-langkah berikut:

### 1. Clone atau Download Repository

```bash
git clone [https://github.com/username/repository-name.git](https://github.com/username/repository-name.git)
cd repository-name

```

### 2. Install Dependencies

Pastikan Python sudah terinstal, lalu jalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt

```

### 3. Konfigurasi Token Lokal

Buat file bernama `.env` di direktori yang sama, lalu tambahkan token bot Anda (pisahkan dengan koma jika lebih dari satu):

```env
DISCORD_TOKEN=token_bot_pertama,token_bot_kedua

```

### 4. Jalankan Bot

```bash
python main.py

```

---

## ☁️ Panduan Deploy 24/7 di Railway

> [!NOTE]
> Railway menyediakan opsi yang sangat stabil untuk menjalankan bot Discord Python 24 jam nonstop secara gratis.

### Langkah 1: Hubungkan Repository ke Railway

1. Akses [Railway Dashboard](https://railway.app/) dan login dengan akun GitHub Anda.
2. Klik tombol **New Project** $\rightarrow$ pilih **Deploy from GitHub repo**.
3. Pilih repository bot ini dari daftar repositori Anda.

### Langkah 2: Menambahkan Token di Environment Variables Railway

1. Di dalam dashboard service Railway Anda, buka tab **Variables**.
2. Klik **+ New Variable** dan tambahkan variabel berikut:
* **Key:** `DISCORD_TOKEN`
* **Value:** Masukkan token bot Discord Anda. Jika menggunakan **banyak bot**, pisahkan dengan koma `,` tanpa spasi.



> [!TIP]
> **Format Value Token:**
> ```env
> Njg5...token1,OTAy...token2,MTAx...token3
> 
> ```
> 
> 

### Langkah 3: Deployment & Verifikasi

1. Railway akan mendeteksi `requirements.txt` secara otomatis dan memulai proses *build*.
2. Buka tab **Logs** untuk memverifikasi bahwa bot telah berhasil terhubung.
3. Contoh output log sukses:
```bash
[ONLINE] Bot #1 is logged in as TimeBot#1234
[STATUS - Bot #1] Updated to: Watching Time 14:00 WIB | Afternoon Vibes ☀️

```



---

## 🔒 Keamanan

> [!WARNING]
> **Jangan pernah** memasukkan/menuliskan token Discord secara mentah (*hardcode*) di dalam berkas kode `.py` atau mem-push token Anda ke repositori GitHub publik. Gunakan selalu **Environment Variable** `DISCORD_TOKEN`.

---

## 📄 Lisensi

Proyek ini dilindungi di bawah lisensi [MIT License](https://www.google.com/search?q=LICENSE). Bebas untuk digunakan, dimodifikasi, dan didistribusikan kembali.
```
