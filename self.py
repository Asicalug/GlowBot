import time
import datetime
from discord.ext import commands

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

timestamp = datetime.datetime.now()
@client.listen()
async def on_message(message):
    if message.content == "time":
        await message.edit(content=f'Year : {timestamp.year},\n Month : {timestamp.month},\n Day : {timestamp.day},\n Hour : {timestamp.hour},\n Minutes : {timestamp.minute},\n Seconds : {timestamp.second},\n Microseconds : {timestamp.microsecond}, \n :warning: **__THIS IS NOT ACCURATE IT HAS BEEN DETERMINED FROM WHEN THE CODE HAS BEEN STARTED.__** *because datetime module is weird.*')
        print(f"just to check if it's discord : {timestamp}")

@client.command()
async def spam(ctx, message=None, amount=None):
    if message==None:
        return await ctx.send("Please enter a message")
    if amount==None:
        return await ctx.send("Please enter the amount of times you want to send this message")
    for i in range(int(amount)):
        time.sleep(0.9)
        await ctx.send(message)


client.run("NzAxMzg4OTEyNTk3NDAxNjIw.GViFZa.P4dafyIbqiGd2rIieWIoS4dBZ6FvHtdESOYzeg") 