import discord
from discord.ext import commands
import os
import random

# 1. Adım: Intent Ayarları
intents = discord.Intents.default()
intents.message_content = True 

# 2. Adım: Bot Tanımlama
bot = commands.Bot(command_prefix=['$', '!'], intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'-----------------------------------')
    print(f'{bot.user} olarak giriş yaptık!')
    print(f'Sistem aktif, komutlar dinleniyor...')
    print(f'-----------------------------------')

# --- Komutlar ---

@bot.command()
async def meme(ctx):
    try:
        # images klasöründeki dosyaları listele
        resimler = os.listdir('images')
        # içlerinden rastgele birini seç
        rastgele_resim = random.choice(resimler)
        
        # Dosyayı açarken basit bir birleştirme kullandık (+)
        with open('images/' + rastgele_resim, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except:
        # Hata olursa uzun uzun yazmak yerine kısa bir mesaj
        await ctx.send("Hata: resim dosyası açılamadı!")

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!', mention_author=True)

@bot.command()
async def selam(ctx):
    await ctx.send(f'Naber! Nasıl gidiyor sana nasıl yardım edebilirim :)')

@bot.command()
async def fnafın_en_güçlü_karakteri_kimdir(ctx):
    await ctx.send(f'Bence lore açısından Springtrap ama fiziksel olarak Golden Freddy')

@bot.command()
async def teşekkürler(ctx):
    await ctx.send(f'Rica Ederim :D')

@bot.command()
async def fnafın_hikayesini_anlat(ctx):
    # FNaF 4, Sister Location ve FFPS dahil edilmiş tam kronoloji
    
    bolum_1 = """
**1. Perde: Kabuslar ve Yer Altındaki Sır (FNaF 4 & Sister Location)**
Her şey 1983'teki **'83 Isırığı** ile başladı. William Afton'ın küçük oğlu (Crying Child), abisi Michael yüzünden can verdi. 

* **FNaF 4:** Küçük çocuğun hastanedeki son günlerinde gördüğü korkunç halüsinasyonlar (Nightmare animatronikleri), babasının onu korkutmak için kurduğu bir deney düzeneği olabilir.
* **Sister Location:** William, çocukları yakalamak için tasarladığı "Funtime" animatroniklerini yaptı. Ancak kızı Elizabeth, Circus Baby tarafından yakalanıp öldü. William, oğlu Michael'ı yer altındaki tesise gönderdi. Michael burada içi boşaltılarak **Ennard** tarafından bir "deri ceket" gibi kullanıldı, ama Remnant (Ruh Özü) sayesinde ölmedi ve mor bir zombi olarak yaşamaya devam etti.
"""

    bolum_2 = """
**2. Perde: Kanlı Geçmiş ve Bahar Kilitleri (FNaF 1, 2 & 3)**
William, Freddy Fazbear's Pizza'da 5 çocuğu öldürdü. Bu çocuklar Puppet aracılığıyla animatroniklere hapsoldu.

* **FNaF 2 & 1:** Yıllar süren intikam arayışı başladı. Animatronikler, katillerini bulmak için her gece bekçisine saldırdı.
* **FNaF 3:** William, kanıtları yok etmek için restorana dönüp robotları parçaladı ama ruhlar serbest kaldı. Korkudan **Spring Bonnie** kostümüne sığındı, kilitler patladı ve 30 yıl boyunca o odada acı içinde bekleyerek **Springtrap**'e dönüştü. Michael ise babasını bulup bu kabusu bitirmek için izini sürdü.
"""

    bolum_3 = """
**3. Final: Alevler ve Arınma (FFPS - Freddy Fazbear's Pizzeria Simulator)**
Henry Emily, hayatta kalan tüm parçaları (Scrap Baby/Elizabeth, Molten Freddy/Ennard, Springtrap/William ve Lefty/Puppet) bir araya toplamak için sahte bir restoran kurdu.

* **Büyük Yangın:** Michael Afton, bu restoranın müdürü olarak işe girdi. Henry, tüm çıkışları kapatıp binayı ateşe verdi.
* **Son Söz:** Henry, kızı Charlie'nin ve diğer çocukların ruhlarını serbest bıraktı. Michael huzura kavuştu, William ise cehennemin en derin katmanına (UCN) gönderildi. Henry'nin planı kusursuzdu... En azından **Glitchtrap** dijital dünyaya sızana kadar.
"""

    await ctx.send(bolum_1)
    await ctx.send(bolum_2)
    await ctx.send(bolum_3)

# Token'ını buraya yapıştır
bot.run("-")
