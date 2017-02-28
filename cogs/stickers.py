from discord.ext import commands
import discord

class Stickers():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stickers(self, ctx):
        await ctx.send("available stickers are: " +
                       "shame-squad, shame-at, bells-of-shame, box-of-shame, shame-spotlight, shame-on you, kickin, "
                       "paddle, spank")

    @commands.command(name="shame-squad")
    async def shamesquad(self, ctx):
        await ctx.send("https://i.imgur.com/1ng02Ft.jpg")

    @commands.command(name="shame-at")
    async def shameat(self, ctx):
        await ctx.send("https://i.imgur.com/zy7GH0Z.jpg")

    @commands.command(name="bells-of-shame")
    async def bellsofshame(self, ctx):
        await ctx.send("https://i.imgur.com/PkXBQuK.jpg")

    @commands.command(name="box-of-shame")
    async def boxofshame(self, ctx):
        await ctx.send("https://i.imgur.com/X0OrYg9.jpg")

    @commands.command(name="shame-spotlight")
    async def shamespotlight(self, ctx):
        await ctx.send("https://i.imgur.com/O1qhuh8.jpg")

    @commands.command(name="shame-on-you")
    async def shameonyou(self, ctx):
        await ctx.send("https://images.discordapp.net/.eJwlzMENwyAMAMBdGAA3OBiSbRBBhCrUCLuvqrtXVb73uI95z8vs5lQdsgMcTTLPw4ryTLXYylyvkkYTm7lDUk357OWlAi76lQgJN3S4LN7jTWEjHyNSiME9oPV_8xzVfH_BiiHj.dvWVpMM2KvqjnGG3fE9PkpuGhEk")

    @commands.command(name="kickin")
    async def kickin(self, ctx):
        await ctx.send("https://images.discordapp.net/.eJwFwVEOgyAMANC7cABaKgzmbQgSNNOWQI0fy-6-977mHqdZza7a5wqwHbPI2OxUGblV20TaWXM_pi1yQVbNZb8q6wTyC2Gk-IouogvoESiFsLxdSN7HlIgCws0flodt52Z-fwV_ItQ.-zzw6mYRiTQejWv6LMD6suSLXCQ")

    @commands.command(name="paddle")
    async def paddle(self, ctx):
        await ctx.send("https://images.discordapp.net/.eJwNxFEOgyAMANC7cABaEAS9DQGCLmgJ7bKPZXef7-N91Xt2tatDZPAOUE7ONItmoZla1Y2o9ZrGyTrTBUkk5eOqtzBYt1gMNqzBBDQeHYKN3i-4PW8uRkQ0UOhzd0pFv0ZTvz8nYSMS.loTYhcCk8TrN7kT0zLOwjDzVq-E")

    @commands.command(name="spank")
    async def spank(self, ctx):
        await ctx.send("https://images.discordapp.net/.eJwVzNsNwyAMAMBdGADzcqDZBhFEiEKMsPtVdfeqN8B91HvdalenyOQd4OhcaB2ahVZuVTeidtc8O-tCA7JILueojzC44J2JLm7RRmPRBAMuIQaD3qb02jx6l6CPf3PNpr4_vR8hwg.2R6_FlLq21NM_nng_SS58PuBzOY")

def setup(bot):
    bot.add_cog(Stickers(bot))