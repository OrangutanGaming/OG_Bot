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

prefix=["?"]
bot = commands.Bot(command_prefix=prefix, description="Orangutan Gaming's bot")

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

startup_extensions = ["cogs.clear", "cogs.dev", "cogs.info", "cogs.count", "cogs.welcome"]

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
    if message.author == message.guild.me:
        return
    if message.author.bot:
        return
    else:
        if message.content.startswith("\o\\"):
            await message.channel.send("/o/")
            return
        elif message.content.startswith("/o/"):
            await message.channel.send("\o\\")
            return
        elif message.content.startswith("\o/"):
            await message.channel.send("\o/")
            return
    await bot.process_commands(message)

bot.remove_command("help")
@bot.command()
async def help(ctx):
    await ctx.send("OG_Bot by Orangutan Gaming `(OGaming#7135)`"
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
async def load(ctx, extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)), delete_after=3)
        return
    await ctx.send("{} loaded.".format(extension_name), delete_after=3)

@bot.command()
async def unload(ctx, extension_name : str):
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name), delete_after=3)

@bot.command()
async def join(ctx):
    options=["This bot is currently a work in progress. It is not public yet. If you're interested in "
                  "helping with testing or have any ideas, PM OGaming#7135",
             "Anyone with the permission `Manage server` can add me to a server using the following link: " + BotIDs.URL]
    DServer="https://discord.gg/duRB6Qg"
    await ctx.send(options[1]+"\nYou can also join the Discord channel at: "+DServer+"\nYou can also help contribute to "
                                                                                    "me at: "+BotIDs.GitHub)

    embed = discord.Embed(description="No message found")
    await ctx.send(embed=embed)
    await ctx.message.delete
    return

# @bot.command()
# async def quote(channel, msgID):
#    async for message in bot.logs_from(channel):
#        if message.id == msgID:
#            quote = message
#            embed = discord.Embed(description=quote.content)
#            embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
#            embed.timestamp = quote.timestamp
#            await ctx.message.delete
#            await ctx.send(embed=embed)
#        if not quote:
#            continue

#
# @bot.command()
# @commands.has_permissions(manage_guild=True)
# async def giveaway(action):
#     if action == "enable":
#         r.db("OG_Bot")r.table("giveaway").insert([])
#     elif action == "disable":
#         #
#     elif action == "clear":
#         #

# @bot.command()
# async def enter

@bot.command()
async def github(ctx):
    await ctx.send("You can join the GitHub using {}".format(BotIDs.GitHub))

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
        await ctx.message.channel.send(error)
    # elif isinstance(error, commands.errors.CommandNotFound):
    #     await message.channel.send("`{}` is not a valid command".format(ctx.invoked_with))
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(error)
    else:
        print(error)

bot.run(BotIDs.token)