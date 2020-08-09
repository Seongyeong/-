import discord

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


client.run("NzQyMDk1Nzc0OTg4NTAxMDAz.XzBIjA.i07wMN6RsGnVyC02alHu9OpwrEE")

