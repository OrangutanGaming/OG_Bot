import discord
import asyncio
from discord.ext import commands
import BotIDs
import logging
import traceback
import rethinkdb as r
import datetime
#import os

#r.connect("localhost", 28015).repl()

bot = commands.Bot(command_prefix="?", description="Orangutan Gaming's bot")

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

startup_extensions = ["cogs.clears", "cogs.dev"]

@bot.event
async def on_ready():
    gamename="with OG|?help"
    await bot.change_presence(game=discord.Game(name=gamename))
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    print("Playing", gamename)
    print(BotIDs.URL)

@bot.event
async def on_message(message):
    if message.author == message.server.me:
        return
    if message.author.bot:
        return
    else:
        if message.content.startswith("\o\\"):
            await bot.send_message(message.channel, "/o/")
            return
        elif message.content.startswith("/o/"):
            await bot.send_message(message.channel, "\o\\")
            return
        elif message.content.startswith("\o/"):
            await bot.send_message(message.channel, "\o/")
            return
    await bot.process_commands(message)

bot.remove_command("help")
@bot.command()
async def help():
    await bot.say("OG_Bot by Orangutan Gaming `(OGaming#7135)`"
                  "\nPrefixes:`?`"
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
                  "\n`botclear`/`bclear` (amount) [Manage Messages]: Deletes the amount of messages given by me in the "
                  "current channel. Default: 100"
                  "\n`clear`/`del`/`delete`/`wipe` (amount) [Manage Messages]: Deletes the amount of messages given in "
                  "the current channel. Default: 100"
                  "\n`github`: Displays GitHub Link")

@bot.command()
async def load(extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)), delete_after=3)
        return
    await bot.say("{} loaded.".format(extension_name), delete_after=3)

@bot.command()
async def unload(extension_name : str):
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name), delete_after=3)

"""
@bot.command(pass_context=True)
async def dev(ctx):
    """
    #Command Use: For Dev to be able to get perms on a server for debugging purposes easily
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
async def pvp(*args, role: discord.Role = None): #args are all the names of the roles with spaces and Capitals
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
"""

#@bot.command(pass_context=True)
#async def roles_change(ctx, roles: discord.Role):
#    bot.edit_role(ctx.message.server, roles)#, permissions=administrator)

@bot.command()
async def join():
    options=["This bot is currently a work in progress. It is not public yet. If you're interested in "
                  "helping with testing or have any ideas, PM OGaming#7135",
             "Anyone with the permission `Manage Server` can add me to a server using the following link: " + BotIDs.URL]
    DServer="https://discord.gg/duRB6Qg"
    await bot.say(options[1]+"\nYou can also join the Discord channel at: "+DServer+"\nYou can also help contribute to "
                                                                                    "me at: "+BotIDs.GitHub)

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
    if counter == 100:
        await bot.edit_message(tmp, "{} has at least {} messages in {}".format(user.mention, counter, channel.mention))
    elif counter <= 99:
        await bot.edit_message(tmp, "{} has {} messages in {}".format(user.mention, counter, channel.mention))
    else:
        await bot.edit_message(tmp, "Counter Bug")

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
        await bot.edit_message(tmp, "There are at least {} messages in {}".format(counter, channel.mention))
    elif counter <= 99:
        await bot.edit_message(tmp, "There are {} messages in {}".format(counter, channel.mention))
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

#@bot.command(pass_context=True)
#async def quote(channel, msgID):
#    async for message in bot.logs_from(channel):
#        if message.id == msgID:
#            quote = message
#            embed = discord.Embed(description=quote.content)
#            embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
#            embed.timestamp = quote.timestamp
#            await bot.delete_message(ctx.message)
#            await bot.say(embed=embed)
#        if not quote:
#            continue

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

#@bot.command(pass_context=True)
#async def serverinfo(ctx):
#    server = ctx.message.server
#
#    embed = discord.Embed(title="Server Info for {}".format(serverinfo.__name__))
#
#    embed.set_image(url=serverinfo.avatar_url)
#    embed.set_footer(text=("Server Created at " + serverinfo.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
#
#    embed.add_field(name="ID", value=serverinfo.id)
#
#    counter = 0
#    for role in server.roles:
#        if role.name == '@everyone':
#            continue
#        counter+=1
#
#    embed.add_field(name="Roles",
#                    value=counter)
#    embed.add_field(name="Avatar URL", value=member.avatar_url)
#
#    await bot.say(embed=embed)

@bot.command(pass_context=True, aliases=["bclear"])
async def botclear(ctx, amount=100):
    if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:

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

    else:
        await bot.say("You must have the `Manage Messages` permission in order to run that command")

"""
@bot.command(pass_context=True, aliases=["del", "delete", "wipe"])
async def clear(ctx, user: discord.User = None, channel: discord.Channel = None, amount=100):

    if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:


        if not channel:
            channel = ctx.message.channel

        try:
            async for message in bot.logs_from(channel, limit=amount, before=ctx.message, reverse=True):
                Time = message.timestamp
                break

            timeMsg = datetime.date(Time)
            Today = datetime.date.today()
            Age = timeMsg - Today
            if Age <= 14:
                    count = 0
                    async for message in bot.logs_from(channel, limit=amount, before=ctx.message):
                        if not user:
                            await bot.delete_message(message)
                            count += 1
                        else:
                            if message.author == user:
                                await bot.delete_message(message)
                                count += 1
                            else:
                                continue
            else:
                await bot.say("Those messages are too old")
                return
            if count == 1:
                tmp = await bot.say("Deleted {} message".format(count))
            else:
                tmp = await bot.say("Deleted {} messages".format(count))
            await asyncio.sleep(3)
            await bot.delete_messages([tmp, ctx.message])


        except discord.Forbidden as error:
            await bot.say("{} does not have permissions".format(bot.user.name))

    else:
        await bot.say("You must have the `Manage Messages` permission in order to run that command")
"""

"""
@bot.command(pass_context=True, aliases=["del", "delete", "wipe"])
async def clear(ctx, user: discord.User = None, channel: discord.Channel = None, amount=100):
    to_delete = []
    cutoff = datetime.datetime.now() - datetime.timedelta(days=14, seconds=-10)

    try:
        async for message in bot.logs_from(channel, after=cutoff):
            if user is None or message.author == user:
                to_delete.append(message)
            if len(to_delete) >= amount:
                break

            count = len(to_delete)

            while to_delete:
                await bot.delete_messages(to_delete[:amount])
                to_delete = to_delete[amount:]

            await bot.say("Deleted {} messages".format(count), delete_after=3)

    except discord.Forbidden as error:
        await bot.say("{} does not have permissions".format(bot.user.name), delete_after=3)
"""

#@bot.command()
#async def

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

@bot.command()
async def github():
    await bot.say("You can join the GitHub using {}".format(BotIDs.GitHub))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.send_message(ctx.message.channel, error)
    #elif isinstance(error, commands.errors.CommandNotFound):
        #await bot.send_message(ctx.message.channel, "`{}` is not a valid command".format(ctx.invoked_with))
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(error)
    else:
        print(error)

bot.run(BotIDs.token)