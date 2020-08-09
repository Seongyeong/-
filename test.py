import discord
import os

client = discord.client()


@clieant.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("test")
    await client.change_pressence(status=discord.Status.online, activty=game)


@client.event
async def on_messag(message):
    if message.content.startswich("드르륵"):
        await message.channel.sand("그래")

        
        
access_token = os.environ["bot_TOKEN"]
client.run("NzQyMDk1Nzc0OTg4NTAxMDAz.XzBIjA.uLMKITJON94QhOuVjNHFTNgOq1k")
