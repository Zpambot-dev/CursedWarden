import discord
from discord.ext.commands import Cog
from warden import client

class EventHandler(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Cog Event Handler is ready")

    @Cog.listener()
    async def on_member_join(self, member):
        print("event MemberJoinEven triggered")
        welcomeChannel = client.get_channel(820937112354422815)
        await welcomeChannel.send(f"{member.display_name} has joined!")

    @Cog.listener()
    async def on_member_remove(self, member):
        print("event MemberLeaveEvent triggered")
        goodbye_channel = client.get_channel(821054437828460574)
        await goodbye_channel.send(f"{member.name} left :(")

def setup(client):
    client.add_cog(EventHandler(client))
