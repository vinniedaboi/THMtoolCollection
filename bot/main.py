import discord 
client = discord.Client()
async def on_ready():
    print("bot is ready".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('^hello'):
        await message.channel.send("HI")
client.run('ODgxODA5NjYyNzYzMjA4NzE1.YSyPPg.Ndl4KxMFAaY1bvEhzvgIV3VqE00')