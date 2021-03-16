import discord
from warden import client
from discord import Embed
from discord import Color
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import cooldown


class Forms(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Cog Forms is ready")

    @command(name = 'apply', help = "Use this to apply using a form")
    @cooldown(1, 10.0)
    async def apply(self, ctx):

        guild = ctx.guild
        member =  guild.get_member(574575329679507466)
        formEmbed = Embed(title = "Application form", description = "Follow the instructions and answer the questions. Your application will be submitted to a staff member for approval.", color = 0x0000ff)
        formEmbed.add_field(name = "Are you sure you want to apply? Trolling may or may not result in punishment", value = "Respond with y/n")
        await ctx.send(embed = formEmbed)
        input = await client.wait_for('message', check = lambda message: message.author == ctx.author)
        
        
        if input.content == 'y':
            
            await ctx.send(f"{ctx.author.name} check your DMs to complete the application!")

            embed = Embed(title = "Application", description = "Fill out the details by responding to the questions below", color = Color.dark_red())
            embed.add_field(name = "What are you applying for?", value = "Moderator, Server Helper, staff member", inline = False)
            embed.add_field(name = "How old are you", value = "Reply with your age for this field", inline = False)
            embed.add_field(name = "Have you properly read the discord TOS?", value = "You will not be accepted if you haven't and can be removed for going against it, should you be accepted. Reply with yes or no", inline = False)
            embed.set_footer(text = "Respond to each field with a seperate line or youre application becomes hard to read. You may be rejected if you reply to all fields with a single answer")

            await ctx.author.send(embed = embed)

            purpose = await client.wait_for('message', check = lambda message: message.author == ctx.author)
            await ctx.author.send(f"Response recorded as: {purpose.content}")
            contentEmbed = Embed(title = " New Application", description = "A new application has been registered", color = Color.dark_purple())
            contentEmbed.add_field(name= "Applicant's name: ", value = f"{ctx.author.name}#{ctx.author.discriminator}", inline = False)
            contentEmbed.add_field(name = "Applicant is in server: ", value = ctx.guild.name, inline = False)
            contentEmbed.add_field(name = "Application purpose: ", value = purpose.content, inline=False)
            age = await client.wait_for('message', check = lambda message: message.author == ctx.author)
            await ctx.author.send(f"Response recorded as: {age.content}")
            contentEmbed.add_field(name = "Applicant age: ", value = age.content, inline = False)
            yOrN = await client.wait_for('message', check = lambda message: message.author == ctx.author)
            await ctx.author.send(f"Response recorded as: {yOrN.content}")
            contentEmbed.add_field(name = "In accordance with TOS?: ", value = yOrN.content, inline=False)

            await ctx.author.send("Thanks for filling out the form!!")


            
            
            
            

            await member.send(embed = contentEmbed)
            

        elif input.content == 'n':
            cancelEmbed = Embed(title = "Your application was cancelled", description = "Your application was successfully cancelled. Thanks for using Cursed Warden!")
            await ctx.send(embed = cancelEmbed)
        else:
            await ctx.send("It seems you've entered an invalid answer. Your application has been cancelled. You can use the command again to re-apply")

def setup(client):
    client.add_cog(Forms(client))
