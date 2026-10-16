import os
import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz

intents = discord.Intents.none()
intents.guilds = True 

bot = commands.Bot(command_prefix="!", intents=intents)
WIB = pytz.timezone("Asia/Jakarta")

@tasks.loop(hours=1)
async def perbarui_status_jam():
    await bot.wait_until_ready()
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
    await bot.change_presence(status=discord.Status.online, activity=aktivitas)
    print(f"[STATUS] Updated to: Watching Time {jam_menit} | {keterangan}")

@bot.event
async def on_ready():
    print(f"[ONLINE] Bot is logged in as {bot.user.name}")
    if not perbarui_status_jam.is_running():
        perbarui_status_jam.start()
    print("[LOG] Bot activity is active (no channel messages).")

TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("[ERROR] DISCORD_TOKEN not found!")
