import os
import asyncio
import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz

WIB = pytz.timezone("Asia/Jakarta")

# Mengambil banyak token dari environment variable (dipisahkan koma)
tokens = [t.strip() for t in os.getenv("DISCORD_TOKEN", "").split(",") if t.strip()]

if not tokens:
    print("[ERROR] DISCORD_TOKEN not found or empty!")
    exit(1)

class TimeBot(commands.Bot):
    def __init__(self, token_str, bot_index):
        intents = discord.Intents.none()
        intents.guilds = True
        super().__init__(command_prefix="!", intents=intents)
        self.token_str = token_str
        self.bot_index = bot_index

    async def setup_hook(self):
        # Memulai loop task untuk masing-masing bot instance
        if not self.perbarui_status_jam.is_running():
            self.perbarui_status_jam.start()

    @tasks.loop(hours=1)
    async def perbarui_status_jam(self):
        await self.wait_until_ready()
        waktu_sekarang = datetime.now(WIB)
        jam_menit = waktu_sekarang.strftime("%H:00 WIB")
        jam_angka = waktu_sekarang.hour

        if 5 <= jam_angka < 11:
            keterangan = "Morning Vibes 🌅"
        elif 11 <= jam_angka < 15:
            keterangan = "Afternoon Vibes ☀️"
        elif 15 <= jam_angka < 18:
            keterangan = "Evening Vibes 🌇"
        else:
            keterangan = "Night Vibes 🌌"

        aktivitas = discord.Activity(
            type=discord.ActivityType.watching,
            name=f"Time {jam_menit}",
            state=keterangan
        )
        await self.change_presence(status=discord.Status.online, activity=aktivitas)
        print(f"[STATUS - Bot #{self.bot_index}] Updated to: Watching Time {jam_menit} | {keterangan}")

    async def on_ready(self):
        print(f"[ONLINE] Bot #{self.bot_index} is logged in as {self.user.name}")

    async def run_bot(self):
        await self.start(self.token_str)

async def main():
    # Menjalankan semua bot secara bersamaan (asinkron)
    bot_instances = [TimeBot(token, i + 1) for i, token in enumerate(tokens)]
    await asyncio.gather(*(b.run_bot() for b in bot_instances))

if __name__ == "__main__":
    asyncio.run(main())
