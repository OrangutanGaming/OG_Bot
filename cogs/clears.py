from discord.ext import commands
import discord
import datetime

class Clears():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["del", "delete", "wipe"])
    async def clear(self, ctx, amount = 100, user: discord.User = None, channel: discord.Channel = None):
        to_delete = []
        cutoff = datetime.datetime.now() - datetime.timedelta(days=14, seconds=-10)
        if not channel:
            channel = ctx.message.channel
        if amount > 100:
            amount = 100
        try:
            async for message in self.bot.logs_from(channel, after=cutoff, limit=amount):
                if user is None or message.author == user:
                    to_delete.append(message)
                if len(to_delete) >= amount:
                    break

                count = len(to_delete)

                while to_delete:
                    await self.bot.delete_messages(to_delete[:amount])
                    to_delete = to_delete[amount:]

                await self.bot.say("Deleted {} messages".format(count), delete_after=3)

        except discord.Forbidden as error:
            await self.bot.say("{} does not have permissions".format(self.bot.user.name), delete_after=3)

def setup(bot):
    bot.add_cog(Clears(bot))