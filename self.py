from discord.ext import commands
import secrets

client = commands.Bot(command_prefix=[">", "!", ".", ":", "-", "^", "/"], self_bot=True)


#@client.event
#async def on_message(message):
#    print(f'USER - {message.author} texted - {message.content}')

@client.command()
async def cmd(ctx):
    await ctx.send("powershell")

@client.listen()
async def on_message(message):
    if  message.content == "faq":
        await message.edit(content="<#1020106859300016188>")

@client.command()
async def spam(ctx, message=None, amount=None):
    if message==None:
        return await ctx.send("Please enter a message")
    if amount==None:
        return await ctx.send("Please enter the amount of times you want to send this message")
    for i in range(int(amount)):
        await ctx.send(message)


client.run(secrets.SELF_TOKEN)