import discord
from discord.ext.commands import Cog
from discord.ext import commands
from warden import client



class ErrorHandler(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Cog Error Handler is ready")

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"That command is on cooldown: `{error}`")
        else:
            raise error


def setup(client):
    client.add_cog(ErrorHandler(client))
