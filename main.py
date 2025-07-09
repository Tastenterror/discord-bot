import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

fragen_liste = [
    "👋 Willkommen! Bitte beantworte folgende Fragen:",
    "1️⃣ Wie lautet dein Ingame-Name?",
    "2️⃣ Was ist dein Anliegen?",
    "3️⃣ Seit wann besteht das Problem?",
    "4️⃣ Hast du Screenshots oder andere Beweise?",
]

@bot.event
async def on_guild_channel_create(channel):
    if "ticket" in channel.name.lower():
        for frage in fragen_liste:
            await channel.send(frage)
            await asyncio.sleep(1.5)  # 1,5 Sekunden Pause dazwischen

bot.run("DEIN_BOT_TOKEN_HIER")
