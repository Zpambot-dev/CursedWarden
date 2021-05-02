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
    @commands.guild_only()
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
        
    @commands.command(name = 'source', aliases = ['s', 'source-code', 'code', 'repo'], help = "Use this command to look at the source code of CursedWarden")
    async def source(self, ctx):
        embed = Embed(title = "CursedWarden's source code", description = "CursedWarden is a completely open-source bot whose code can be found on github", color = Color.magenta())
        embed.add_field(name = "Find the source code on GitHub!", value = "[click here](https://github.com/Zpambot-dev/CursedWarden/tree/main) to view CursedWarden's source code")
        embed.set_footer(text = "Feel free to do whatever you want with this code!!")
        await ctx.send(embed = embed)


    


        
def setup(client):
    client.add_cog(Misc(client))
