import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

fragen_liste = [
    "1️⃣ Wie lautet dein Ingame-Name?",
    "2️⃣ Was ist dein Anliegen?",
    "3️⃣ Seit wann besteht das Problem?",
    "4️⃣ Hast du Screenshots oder andere Beweise?",
]

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel) and "ticket" in channel.name.lower():
        try:
            await channel.send("👋 Willkommen! Bitte beantworte folgende Fragen:")
            for frage in fragen_liste:
                await channel.send(frage)
        except Exception as e:
            print(f"Fehler beim Senden: {e}")

token = os.getenv("TOKEN")
if not token:
    raise RuntimeError("TOKEN ist nicht gesetzt als Umgebungsvariable.")
bot.run(token)
