import nextcord
from nextcord.ext import commands, tasks
from nextcord.ui import Select, View
from nextcord import Interaction, components, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from itertools import cycle
 
 
 
#pip install -U git+https://github.com/Rapptz/nextcord.py
 
 
 
intents = nextcord.Intents().all()
client = commands.Bot(command_prefix = ('G-','g-'), intents=intents)
client.remove_command('help')

testingServerID = 966792562671230986
 
status = cycle(['Watching Discord','Watching for g-','Having fun','g-help or G-help'])
 
#--------------------------------
#=============embeds=============
#--------------------------------

HelpCommandEmbed = nextcord.Embed(title='Help',description='Here is the help!', color=nextcord.Color.green())
HelpCommandEmbed.add_field(name='g- or G-', value="this is the default prefix",inline=False)
HelpCommandEmbed.add_field(name='help', value='The help command shows this message. ("<>" = **REQUIRED**, "()" = **OPTIONAL**', inline=False)
HelpCommandEmbed.add_field(name='ping', value='sends "Pong!"', inline=False)
HelpCommandEmbed.add_field(name='kick', value='<@"__User__"> (reason)|Kicks a member.', inline=False)
HelpCommandEmbed.add_field(name='ban', value='<@"__User__"> (reason)|Bans a member.', inline=False)
HelpCommandEmbed.add_field(name='unban', value='<@"__Banned User__">|Unbans a banned member.', inline=False)
HelpCommandEmbed.add_field(name='clear', value='<Number of messages (Max. 100)>|Delete more than 100 messsages with one command.', inline=False)
HelpCommandEmbed.add_field(name='mute', value='<@"__User__"> (reason)', inline=False)
HelpCommandEmbed.add_field(name='unmute', value='<@"Muted User"> (reason)|Unmutes a user', inline=False)
HelpCommandEmbed.add_field(name='slowmode', value='<time (Max. 21600)>', inline=False)
HelpCommandEmbed.add_field(name='say', value='<__"message"__>', inline=False)
HelpCommandEmbed.add_field(name='sayembed', value='<__"message"__', inline=False)
HelpCommandEmbed.add_field(name='serverinfo', value='No required argumnts', inline=False)
 
BotInfoEmbed = nextcord.Embed(title='Info', description='Bot  information', color=nextcord.Color.dark_teal())
BotInfoEmbed.add_field(name='General info', value='The bot was coded with Python and nextcord.py', inline=False)
BotInfoEmbed.add_field(name='commands', value='To get a list of the commands you can send <g-help> or <g-selector>', inline=False)
BotInfoEmbed.add_field(name='Slash Commands', value='I am still learning nextcord.py and trying to use Slash commands without hikari.', inline=False)
BotInfoEmbed.add_field(name='Errors', value='If the bot has any errors please report it to the Developper', inline=False)
 
SelectorEmbed = nextcord.Embed(title='Selector', description='Select the command that you want to execute.', color = nextcord.Color.blurple())
 
PingLatencyEmbed = nextcord.Embed(title='Pong!', description=client.latency, color=nextcord.Color.blurple())
 
HiCommandEmbed = nextcord.Embed(title="Hi",description="Hello!", color=nextcord.Color.greyple())
 
IdkCommandEmbed = nextcord.Embed(title="Idk",description="I D'ont Know either!", color=nextcord.Color.blurple())
 
IkCommandEmbed = nextcord.Embed(title="Ik",description="Yeah, I Know", color=nextcord.Color.blurple())
 
MissingRequiredArgumentEmbed = nextcord.Embed(title= "Error", description = "Missing a Required Argument", color = nextcord.Color.red())
 
MemberNotFoundEmbed = nextcord.Embed(title= "Error", description = "Member not found.", color = nextcord.Color.red())
 
IncludeUserEmbed = nextcord.Embed(title= "Error", description = " include the user.", color = nextcord.Color.red())
 
BadArgumentNumberEmbed = nextcord.Embed(title= "Error", description = "Put a valid number.", color = nextcord.Color.red())
 
SayInputTextEmbed = nextcord.Embed(title="Error", description = "You must tell me the message you want to say!", color = nextcord.Color.red())
 
CommandNotFoundEmbed = nextcord.Embed(title= "Error", description = " That command does not exist.", color = nextcord.Color.red())
 
MaxDeletedMessagesEmbed = nextcord.Embed(title = "Error", description= 'Can not delete more than 100 messages.', color = nextcord.Color.red())
 
ClearedMessagesEmbed = nextcord.Embed(title = "Success", description= 'Successfully Cleared Messages.', color = nextcord.Color.green())
 
RequiresPermKickMembersEmbed = nextcord.Embed(title='Error', description='This command requires Kick Members', color=nextcord.Color.red())
 
RequiresPermBanMembersEmbed = nextcord.Embed(title='Error', description='This command requires Ban Members', color =nextcord.Color.red())
 
RequiresManageMessagesEmbed = nextcord.Embed(title='Error', description='This command requires Manage Messages', color =nextcord.Color.red())
 
PingEmbed = nextcord.Embed(title='Ping', description='Pong!', color=nextcord.Color.green())
 
CommandOnCooldownEmbed = nextcord.Embed(title='Error', description='Command is on cooldown. Please wait ... ', color=nextcord.Color.red())
 
InputQuestionEmbed = nextcord.Embed(title='Error', description='You need to put in a question.', color=nextcord.Color.red())
 
InputAnswerEmbed = nextcord.Embed(title='Error', description='You need to put in an answer.', color=nextcord.Color.red())
 
NoIdeaEmbed = nextcord.Embed(title='No idea', description="I d'ont have any idea either", color=nextcord.Color.random())

IdcCommandEmbed = nextcord.Embed(title="I D'ont Care", description="I Don't Care Either Bruh", color=nextcord.Color.dark_gold())

TestEmbed = nextcord.Embed(title="This Is A Test.", description="This Is A Very Good Test LoL", color=nextcord.Color.blurple())
 
@tasks.loop(seconds=20)
async def status_swap():
    await client.change_presence(activity=nextcord.Game(next(status)))
 
#--------------------------------
#=============events=============
#--------------------------------

@client.event
async def on_ready():
    print('Glow is ready.')
    status_swap.start()
 
@client.event
async def on_member_join(member):
 
    welcomeEmbed = nextcord.Embed(title = "New member!!!", description = f"{member.name} has joined the server!", color = nextcord.Color.blue())
 
    await client.get_channel(967071139044147242).send(embed = welcomeEmbed)

#----------------------------------
#=============commands=============
#----------------------------------
 
#@slash.slash(description="Shows the bots latency")
#PingLatencyEmbed = nextcord.Embed(title='Pong!', description=f'Bot Speed - {round(client.latency * 1000)}ms ', color=nextcord.Color.blurple())
#async def ping(ctx):
#    await ctx.send(embed = PingLatencyEmbed)
 
#first slash command
#@app_commands.command(name='slash', description='First / command')
#async def slash(ctx, interaction: nextcord.Interaction, slash: str, slash2: int) -> None:
#    await interaction.response.send_message(f'Slash is: {slash}  nd slash2 is: {slash2}')
 
 
#ping
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def ping(ctx):
    await ctx.send(embed = PingLatencyEmbed)
 
#selectcommand
@client.command()
#@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def selector(ctx):
    select = Select(placeholder='Choose a command!', options=[nextcord.SelectOption(label="help", emoji='<:python:596577462335307777>', description='executes the help command')])
    async def my_callback(interaction):
        await interaction.respond.send_message("g-help")
    select.callback = my_callback
 
    view = View()
    view.add_item(select)
    await ctx.send(embed = SelectorEmbed, view=view)
 
#hi
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def hi(ctx):
    await ctx.send(embed = HiCommandEmbed)
    interaction = await client.wait_for("button_click", check=lambda i: i.component.label.startswith("Click"))
    await interaction.respond(content="Clicked the button.")
 
#spam
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def spam( ctx, message=None, times=None):
    for i in range(int(times)):
        await ctx.send(message)

#idk
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def idk(ctx):
    await ctx.send(embed = IdkCommandEmbed)
 
#ik
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def ik (ctx):
    await ctx.send(embed = IkCommandEmbed)

#idc
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def idc(ctx):
    await ctx.send(embed = IdcCommandEmbed)
 
#kick
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def kick(ctx, member:nextcord.Member, *, reason=None):
 
    KickedMemberEmbed = nextcord.Embed(title='Success', description=f'Successfully kicked {member.mention}', color=nextcord.Color.green())
 
    if(not ctx.author.guild_permissions.kick_members):
 
        await ctx.send(embed = RequiresPermKickMembersEmbed)
        return
    await member.kick(reason=reason)
    await ctx.send(embed = KickedMemberEmbed)
 
#ban
@client.command()
@commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
async def ban(ctx, member:nextcord.Member, *, reason=None):
 
    BannedMemberEmbed = nextcord.Embed(title 
    ='Success', description=f'Successfully banned {member.mention}', color=nextcord.Color.green())
 
    if(not ctx.author.guild_permissions.ban_members):
        await ctx.send(embed = RequiresPermBanMembersEmbed)
        return
    await member.ban(reason=reason)
    await ctx.send(embed = BannedMemberEmbed)
 
#unban
@client.command()
 
async def unban(ctx, *, member):
 
    UnbannedMemberEmbed = nextcord.Embed(title 
    ='Success', description=f'Successfully unbanned {member.mention}', color=nextcord.Color.green())
 
    if(not ctx.author.guild_permissions.ban_members):
        await ctx.send(embed = RequiresPermBanMembersEmbed)
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
 
    for ban_entry in banned_users:
        user = ban_entry.user
 
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed = UnbannedMemberEmbed)
            return
 
#clear
@client.command()
async def clear(ctx, amount=11):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = RequiresManageMessagesEmbed)
        return
    amount = amount+1
    if amount > 101:
        await ctx.send(embed = MaxDeletedMessagesEmbed)
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed = ClearedMessagesEmbed)
 
#mute
@client.command()
@commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
async def mute(ctx, member : nextcord.Member, *, reason=None):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed =RequiresManageMessagesEmbed)
        return
    guild = ctx.guild
    muteRole = nextcord.utils.get(guild.roles,name="Muted")
 
    if not muteRole:
        muteRole = await guild.create_role(name="Muted")
 
        for channel in guild.channels:
            await ctx.send('No mute role has been found. Creating  role...')
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    await member.add_roles(muteRole, reason=reason)
    await ctx.send('User Has Been Muted.')
    await member.send(f"You have been muted from {guild.name} | Reason : {reason:}")
 
#unmute
@client.command()
@commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
async def unmute(ctx, member : nextcord.Member, *, reason=None):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('This command requires Manage Messages')
        return
    guild = ctx.guild
    muteRole = nextcord.utils.get(guild.roles,name="Muted")
 
    if not muteRole:
        await ctx.send("The muted role has not been found.")
    await member.remove_roles(muteRole, reason=reason)
    await ctx.send('User Has Been Unmuted.')
    await member.send(f"You have been unmuted from {guild.name} | Reason : {reason}")
 
#slowmode
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def slowmode(ctx, time:int):
 
    slowmodeOnEmbed = nextcord.Embed(title = "Slowmode", description = f"Slowmode has been enabled and set to {time} seconds.", color = nextcord.Color.green())
 
    slowmodeOffEmbed = nextcord.Embed(title= "Slowmode", description = "Slowmode has been disabled.", color = nextcord.Color.red())
 
    slowmodeErrorEmbed = nextcord.Embed(title= "Error",
description = "Can't set slowmode above 6 hours.", color = nextcord.Color.red())
 
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('This command requires Manage Messages')
        return
    try:
        if time == 0:
            await ctx.send(embed = slowmodeOffEmbed)
            await ctx.channel.edit(slowmode_delay = 0)
        elif time > 21600:
                await ctx.send(embed = slowmodeErrorEmbed)
                return
        else:
                await ctx.channel.edit(slowmode_delay = time)
                await ctx.send(embed = slowmodeOnEmbed)
    except  Exception:
                await print('Oops!')
 
#say
@client.command()
@commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
async def say(ctx, msg=None):
    if msg==None:
        return await ctx.send(embed = SayInputTextEmbed)
    await ctx.send(msg)
 
#embed
@client.command()
@commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
async def embed(ctx, title=None, description=None):
 
    SayCommandEmbed = nextcord.Embed(title= f"{title}", description = f"{description}", color = nextcord.Color.random())
 
 
    if description==None:
        return await ctx.send(embed = SayInputTextEmbed)
 
    elif title==None:
        return await ctx.send(embed = SayInputTextEmbed)
    await ctx.send(embed = SayCommandEmbed)
 
#serverinfo
@client.command()
@commands.cooldown(1, 20, commands.cooldowns.BucketType.user)
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot .bot]
 
    serverInfoEmbed = nextcord.Embed(title= "Server Informations", description = "Here are the server infos :", color = nextcord.Color.green())
    serverInfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}")
    serverInfoEmbed.add_field(name='Member Count', value=ctx.guild.member_count)
    serverInfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level))
    serverInfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2])
    serverInfoEmbed.add_field(name='Number of Roles', value=str(role_count))
 
    await ctx.send(embed =
serverInfoEmbed)
 
#bot informations
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def botinfo(ctx):
    await ctx.send(embed = BotInfoEmbed)
 
#quiz
@client.command()
@commands.cooldown(1, 15, commands.cooldowns.BucketType.guild)
async def quiz(ctx, answer:str, question=None):
 
    QuizCommandEmbed = nextcord.Embed(title='Quiz', description=f'The question is : {question} and the answer is ||You Gotta Find it!||', color=nextcord.Color.blurple())
    answer = "{answer}"
 
    if question==None:
        return await ctx.send(embed = InputQuestionEmbed)
 
    elif answer==None:
        return await ctx.send(embed = InputAnswerEmbed)
    await ctx.send(embed = QuizCommandEmbed)
 
@client.command()
@commands.cooldown(1, 2, commands.cooldowns.BucketType.user)
async def answer(ctx, youranswer=None):
    if youranswer==None:
        return await ctx.send('You need to enter a answer with "Your''re answer".')
 
    elif youranswer==answer:
        return await ctx.send("Nop")
#FoundQuizEmbed = nextcord.Embed(title='Winner!!!', description=f'The last message won with the answer: {answer}')
    await ctx.send("yep")
 
 
 
 
#help
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def help(ctx):
    await ctx.send(embed = HelpCommandEmbed)
 
#No idea 
@client.command()
@commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
async def no_idea(ctx):
    await ctx.send(embed = NoIdeaEmbed)
 
#--------------------------------
#=============errors=============
#--------------------------------
 
async def notfound(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(embed = CommandNotFoundEmbed)
 
@help.error
async def error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
 
@kick.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = IncludeUserEmbed)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed = MemberNotFoundEmbed)
    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
 
 
@ban.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = IncludeUserEmbed)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed = MemberNotFoundEmbed)
    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
 
@mute.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = IncludeUserEmbed)
    elif isinstance(error, commands.errors.MemberNotFound):
        await ctx.send(embed = MemberNotFoundEmbed)
 
@unmute.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = IncludeUserEmbed)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed = MemberNotFoundEmbed)
    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
 
@slowmode.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = MissingRequiredArgumentEmbed)
    elif isinstance (error, commands.errors.BadArgument):
        await ctx.send(embed = BadArgumentNumberEmbed)
    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)

@say.error
async def error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = MissingRequiredArgumentEmbed)

@embed.error
async def error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send(embed = CommandOnCooldownEmbed)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = MissingRequiredArgumentEmbed)



#----------------------------------------
#=============Slash Commands=============
#----------------------------------------

#help
@client.slash_command(name="help", description="A list of all the commands and how to use them")#, guild_ids=[testingServerID])
async def help(interaction : Interaction):
    await interaction.response.send_message(embed = HelpCommandEmbed)

#test
@client.slash_command(name="test", description='This Is A Test')#, guild_ids=[testingServerID])
async def test(interaction : Interaction):
    await interaction.response.send_message(embed = TestEmbed)

#repeat 
@client.slash_command(name="say", description='repeats whatever you say') #guild_ids=[testingServerID])
async def repeat(interaction : Interaction, message:str):
    await interaction.response.send_message(f"{message}")

#ping
@client.slash_command(name='ping', description='Says the ping of the bot')#, guild_ids=[testingServerID])
async def ping(interaction : Interaction):
    await interaction.response.send_message(embed = PingLatencyEmbed)

#say
@client.slash_command(name='say', description='Says the message that you typed in "message"')
async def say(interaction : Interaction, message=None):
    if message==None:
        return await interaction.response.send_message(embed = SayInputTextEmbed)
    await interaction.response.send_message(message)
 
#embed
@client.slash_command(name='embed', description='Sends a custom embed')
async def embed(interaction : Interaction, title=None, description=None):
 
    SayCommandEmbed = nextcord.Embed(title= f"{title}", description = f"{description}", color = nextcord.Color.random())
 
 
    if description==None:
        return await interaction.send(embed = SayInputTextEmbed)
 
    elif title==None:
        return await interaction.send(embed = SayInputTextEmbed)
    await interaction.response.send_message (embed = SayCommandEmbed)

#-----------------------------------------------
#===================run bot=====================
#-----------------------------------------------
client.run('OTY2Nzk0NTg2NDM1NTE4NTE0.YmG7nw.7UtfOF7I1tI1M8eps3yLw9r6-3g')