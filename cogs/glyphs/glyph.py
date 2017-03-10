import sqlite3
connect = sqlite3.connect("codes.db")
c = connect.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS codes"
#           "(platform text, code text, id text)")

# c.execute("INSERT INTO codes VALUES ('PC', 'code', 'NULL')")

# connect.commit()

from discord.ext import commands

class Glyph():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def glyph(self, ctx, platform):
        c.execute("select * from codes")

def setup(bot):
    bot.add_cog(Glyph(bot))