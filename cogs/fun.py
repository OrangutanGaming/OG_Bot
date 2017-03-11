from discord.ext import commands
import time

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        pong = await ctx.send("Pong. :ping_pong:")

        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        pingT = (after - before) * 1000
        pingT = str(int(pingT))

        await pong.edit(content="Pong. :ping_pong: **{}ms**".format(pingT))

def setup(bot):
    bot.add_cog(Fun(bot))