import os
import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

intents = discord.Intents.none()
intents.guilds = True 

bot = commands.Bot(command_prefix="!", intents=intents)
WIB = pytz.timezone("Asia/Jakarta")

async def kirim_pengingat_ke_semua(teks_pesan):
    await bot.wait_until_ready()
    for guild in bot.guilds:
        channel_tujuan = None
        for channel in guild.text_channels:
            permissions = channel.permissions_for(guild.me)
            if permissions.send_messages and not channel.is_nsfw():
                channel_tujuan = channel
                break
        
        if channel_tujuan:
            try:
                await channel_tujuan.send(teks_pesan)
                print(f"[LOG] Successfully sent to: {guild.name} -> #{channel_tujuan.name}")
            except Exception as e:
                print(f"[ERROR] Failed sending to {guild.name}: {e}")

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
    
    scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
    scheduler.add_job(lambda: bot.loop.create_task(kirim_pengingat_ke_semua("🌅 Good Morning! Have a great start to your day.")), CronTrigger(hour=6, minute=0))
    scheduler.add_job(lambda: bot.loop.create_task(kirim_pengingat_ke_semua("☀️ Good Afternoon! Don't forget to take a break and have lunch.")), CronTrigger(hour=12, minute=0))
    scheduler.add_job(lambda: bot.loop.create_task(kirim_pengingat_ke_semua("🌇 Good Evening! Time to relax after a busy day.")), CronTrigger(hour=17, minute=0))
    scheduler.add_job(lambda: bot.loop.create_task(kirim_pengingat_ke_semua("🌌 Good Night! Rest well and sweet dreams.")), CronTrigger(hour=21, minute=0))
    
    scheduler.start()
    print("[LOG] Multi-server time scheduler is active.")

TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("[ERROR] DISCORD_TOKEN not found!")
