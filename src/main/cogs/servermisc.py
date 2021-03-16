import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from discord import Color
from warden import client

class ServerMisc(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Cog Server Misc is ready")

    @command(name = 'serverinfo')
    async def serverinfo(self, ctx):
        memberCount = len(ctx.guild.members)
        serverIcon = ctx.guild.icon_url
        serverEmbed = Embed(title= "Server Info", description = "ok", color = Color.gold())
        serverEmbed.add_field(name = "Server Name", value = ctx.guild.name, inline = False)
        serverEmbed.add_field(name = "Server Id", value = ctx.guild.id, inline = False)
        serverEmbed.add_field(name="Number of channels", value = len(ctx.guild.channels), inline = False)

        serverEmbed.add_field(name = "Member Count", value = memberCount)
        serverEmbed.set_thumbnail(url=serverIcon)
        await ctx.send(embed = serverEmbed)


def setup(client):
    client.add_cog(ServerMisc(client))
