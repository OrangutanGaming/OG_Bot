import discord
from discord.ext import commands
import BotIDs
import logging
import traceback
import cogs.utils.prefix as Prefixes
import rethinkdb as r
import datetime
import os

#r.connect("localhost", 28015).repl()

prefixes = Prefixes.prefixes
bot = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes), description="Orangutan Gaming's bot")
bot.remove_command("help")

logger = logging.getLogger("discord")
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

startup_extensions = ["cogs.clear",
                      "cogs.dev",
                      "cogs.info",
                      "cogs.count",
                      "cogs.welcome",
                      "cogs.stickers",
                      "cogs.help",
                      "cogs.fun",
                      "cogs.utils.stats",
                      "cogs.eval",
                      "cogs.edit"
                      ]

@bot.event
async def on_ready():
    gamename="with OG|o!help"
    await bot.change_presence(game=discord.Game(name=gamename))
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    print("Playing", gamename)
    print(BotIDs.URL)
    print("Prefixes: " + Prefixes.Prefix('"'))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    # if message.content.endswith == "":
    #     await message.channel.send("What?")
    #     return
    # else:
    #     if message.content.startswith("\o\\"):
    #         await message.channel.send("/o/")
    #         return
    #     elif message.content.startswith("/o/"):
    #         await message.channel.send("\o\\")
    #         return
    #     elif message.content.startswith("\o/"):
    #         await message.channel.send("\o/")
    #         return
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    try:
        await guild.default_channel.send("Welcome to the world of Orangutans! I was made by `OGaming#7135` Run `o!help` for"
                                     " help")
    except discord.Forbidden:
        return

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
    await ctx.send("\nYou can also help support me at " + BotIDs.Patreon)

@bot.command()
async def support(ctx):
    await ctx.send("You can help support the bot with " + BotIDs.Patreon)

@bot.command()
async def github(ctx):
    await ctx.send("You can join the GitHub using {}".format(BotIDs.GitHub))

# @bot.command()
# async def quote(channel, msgID):
#    async for message in bot.logs_from(channel):
#        if message.id == msgID:
#            quote = message
#            embed = discord.Embed(description=quote.content)
#            embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
#            embed.timestamp = quote.created_at
#            await ctx.message.delete()
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
# async def enter():

# TODO RethinkDB

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
    elif isinstance(error, commands.errors.CommandNotFound):
        # await ctx.message.channel.send("`{}` is not a valid command".format(ctx.invoked_with))
        return
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(error)
    else:
        print(error)

bot.run(BotIDs.token)