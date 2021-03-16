import discord
from discord.ext import commands
from discord import Embed
from discord import Color

deletedMsg = None
author = None

description = None

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Misc is ready")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(f"{message.content} was deleted")
        global deletedMsg 
        global author
        deletedMsg = message.content
        author = message.author

    
    @commands.command(name = 'snipe', aliases = ['w', 'expose'], help = "Expose someone >:)")
    async def snipe(self, ctx):
        global deletedMsg
        if ctx.message.content == "$snipe":
            global description
            description = deletedMsg
        
        sniper = Embed(title = "Snipe", description = description, color = Color.blurple())
        global author 
        thumbnail = author.avatar_url_as(size = 64)
        sniper.set_thumbnail(url=thumbnail).set_footer(text=f"Message sent by {author.name}")
        await ctx.send(embed = sniper)

    


        
def setup(client):
    client.add_cog(Misc(client))
