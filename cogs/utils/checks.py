from discord.ext import commands
import BotIDs

def is_owner_check(ctx):
    return ctx.author.id == BotIDs.ownerID

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx))