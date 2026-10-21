🕒 Multi-Token Discord Time Status Bot
Bot Discord asinkron berbasis Python yang dirancang untuk menjalankan multiple bot instance secara bersamaan dalam satu proses (asyncio). Bot ini otomatis memperbarui status aktivitas (watching status) setiap jam berdasarkan zona waktu WIB (Asia/Jakarta) lengkap dengan penyesuaian suasana waktu (pagi, siang, sore, malam).

Repository ini bersifat publik dan dapat digunakan serta di-deploy dengan mudah secara 24/7 gratis di platform Railway.

✨ Fitur Utama
Multi-Bot Support: Jalankan banyak bot sekaligus hanya dengan memasukkan banyak token yang dipisahkan oleh koma (token1,token2,token3).

Dynamic Time Status: Mengubah status aktivitas bot secara otomatis setiap 1 jam sekali dengan format waktu WIB dan deskripsi vibes yang dinamis:

🌅 Morning Vibes (05:00 - 10:59)

☀️ Afternoon Vibes (11:00 - 14:59)

🌇 Evening Vibes (15:00 - 17:59)

🌌 Night Vibes (18:00 - 04:59)

Asynchronous Engine: Dibangun di atas asyncio dan discord.py versi modern dengan commands.Bot dan setup_hook.

Lightweight Intents: Menggunakan konfigurasi intents.none() dengan hanya mengaktifkan guilds = True agar sangat hemat sumber daya.

🛠️ Requirements
File requirements.txt yang dibutuhkan oleh project ini:

Plaintext
discord.py
pytz
☁️ Panduan Deploy 24/7 Gratis di Railway
Bagi Anda atau pengguna lain yang ingin mendeploy bot ini ke Railway, ikuti langkah-langkah berikut:

Langkah 1: Hubungkan Repository ke Railway
Login ke Railway menggunakan akun GitHub Anda.

Klik tombol New Project -> pilih Deploy from GitHub repo.

Pilih repository publik bot ini.

Langkah 2: Menambahkan Token di Environment Variables Railway
Di halaman dashboard Railway, klik pada service project bot Anda.

Cari dan klik tab Variables di bagian atas menu.

Klik tombol + New Variable (atau isi kolom yang tersedia).

Masukkan konfigurasi variabel sebagai berikut:

Variable Name (Key): DISCORD_TOKEN

Value: Masukkan token bot Discord Anda. Jika menggunakan banyak bot sekaligus, pisahkan token-token tersebut menggunakan tanda koma , tanpa spasi berlebih.

Contoh Value:

Code snippet
OTAxND...xMA.G5-abc,OTAyND...xTQ.H6-def
Klik tombol Add atau Save untuk menyimpan variabel.

Langkah 3: Deployment & Verifikasi
Railway akan secara otomatis membaca file requirements.txt dan melakukan proses build serta deploy sesaat setelah variabel disimpan.

Pindah ke tab Deployments atau Logs untuk memantau proses jalannya bot.

Jika berhasil, Anda akan melihat output log seperti berikut:

Plaintext
[ONLINE] Bot #1 is logged in as NamaBot1
[STATUS - Bot #1] Updated to: Watching Time 14:00 WIB | Afternoon Vibes ☀️
📝 Catatan Penting
Jangan pernah membagikan atau mem-push token Discord Anda langsung ke dalam kode repository GitHub publik. Gunakan selalu Environment Variables (os.getenv("DISCORD_TOKEN")).

Jika Anda mengganti atau menambahkan token baru di Railway, bot akan otomatis melakukan restart dan memuat token yang baru ditambahkan.
