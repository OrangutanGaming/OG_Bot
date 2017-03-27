from discord.ext import commands
import time
import unicodedata

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        pingT = (after - before) * 1000
        pingT = round(pingT)

        await ctx.send("Pong. :ping_pong: **{}ms**".format(pingT))

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):

        if len(characters) > 15:
            await ctx.send(f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.send("\n".join(map(to_string, characters)))

def setup(bot):
    bot.add_cog(Fun(bot))