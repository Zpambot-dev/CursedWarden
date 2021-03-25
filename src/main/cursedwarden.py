import discord
from discord.ext.commands import Bot
import os

intents = discord.Intents.all()
client = Bot(command_prefix="$", intents = intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    await client.change_presence(activity=discord.Game(f"$help| In {len(client.guilds)} servers"), status=discord.Status.do_not_disturb)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run()"""Not that open-source lol"""
