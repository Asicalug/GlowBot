import os
import sys
import time
import secrets
import datetime
import subprocess
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
        time.sleep(1)
        await ctx.send(message)

@client.listen()
async def on_message(ctx):
    if ctx.content.lower()=="bug":
        return await ctx.reply(":fly:")

@client.listen()
async def on_message(ctx):
    values={"asicalug", "@asicalug", "@asicalug#7189", "<@701388912597401620>"}
    if ctx.content.lower() in values: 
        return await ctx.reply("Yes?")

@client.listen()
async def on_message(ctx):
    values={"socket","/socket","/scket","soket","/soket","socet","/socet","scket","webstock"}
    if ctx.content.lower() in values:
        return await ctx.reply("`wss://socket.solartweaks.com`")

@client.listen()
async def on_message(ctx):
    if ctx.content.lower()=="nerd":
        return await ctx.reply(":nerd:")

@client.listen()
async def on_message(ctx):
    values={"where do i download", "/download", "download", "where download?", "where download"}
    if ctx.content.lower() in values:
        return await ctx.reply("https://github.com/Solar-Tweaks/Solar-Tweaks")

@client.command(name= 'restart')
async def restart(ctx):
    await ctx.reply("Restarting...")
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
    sys.argv[1:])

@client.listen()
async def on_message(ctx):
    if ctx.content.lower()=="test2004":
        return await ctx.reply(f"[here](https://youtube.com)")
client.run(secrets.self_TOKEN) 
