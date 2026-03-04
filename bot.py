import discord
from discord.ext import commands
import os  # Sistemden token çekmek için
from flask import Flask  # Koyeb'de uyanık kalması için
from threading import Thread

# --- 1. KOYEB UYANIK TUTMA (KEEP ALIVE) AYARI ---
app = Flask('')

@app.route('/')
def home():
    return "Bot 7/24 Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# -----------------------------------------------

# 2. Adım: Intent (Niyet) Ayarları
intents = discord.Intents.default()
intents.message_content = True 

# 3. Adım: Bot Tanımlama
bot = commands.Bot(command_prefix=['$'], intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'-----------------------------------')
    print(f'{bot.user} (ID: {bot.user.id}) olarak giriş yaptık!')
    print(f'Koyeb üzerinden sistem aktif...')
    print(f'-----------------------------------')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!', mention_author=True)

@bot.command()
async def selam(ctx):
    await ctx.reply(f'Naber! Nasıl gidiyor sana nasıl yardım edebilirim :)', mention_author=True)

@bot.command()
async def fnafın_en_güçlü_karakteri_kimdir(ctx):
    await ctx.reply(f'Bence lore açısından Springtrap ama fiziksel olarak Golden Freddy', mention_author=True)

@bot.command()
async def teşekkürler(ctx):
    await ctx.reply(f'Rica Ederim :D')

@bot.command()
async def fnafın_hikayesini_anlat(ctx):
    bolum_1 = """
**1. Başlangıç: İki Ortak ve İki Kader**
Henry Emily ve William Afton... Her şey Fredbear’s Family Diner ile başladı.
* **İlk Kurban:** William, Henry'nin kızı Charlie'yi öldürdü. Charlie'nin ruhu The Puppet oldu.
* **83 Isırığı:** William’ın küçük oğlu, Fredbear’ın ağzında hayatını kaybetti.
"""
    bolum_2 = """
**2. Kayıp Çocuklar ve Son**
William Afton 5 çocuğu öldürdü, Puppet ruhları animatroniklere yerleştirdi. William en son Spring Bonnie kostümüne sıkışıp **Springtrap** oldu.
"""
    await ctx.reply(bolum_1, mention_author=True)
    await ctx.reply(bolum_2, mention_author=True)

# --- ÇALIŞTIRMA ---
if __name__ == "__main__":
    keep_alive()  # Koyeb'in botu kapatmasını engeller
    # Koyeb panelinde tanımlayacağın isimle çekiyoruz:
    token = os.environ.get('BOT_TOKEN') 
    bot.run(token)
