from discord.ext import commands
import discord

class Count():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mcount"])
    async def msgcount(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        counter = 0
        tmp = await ctx.send("Counting messages...")
        if not user:
            user = ctx.message.author
        if not channel:
            channel = ctx.message.channel
        async for log in channel.history(limit=99, before=ctx.message):
            if log.author == user:
                counter += 1
        await ctx.message.delete()
        counter += 1
        if counter == 100:
            await tmp.edit(content="{} has at least {} messages in {}".format(user, counter, channel.mention))
        elif counter == 1:
            await tmp.edit(content="{} has 1 message in {}".format(user, channel.mention))
        elif counter <= 99:
            await tmp.edit(content="{} has {} messages in {}".format(user, counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")
    
    @commands.command(aliases=["amcount"])
    async def amsgcount(self, ctx, channel: discord.TextChannel = None):
        counter = 0
        tmp = await ctx.send("Counting messages...")
        if not channel:
            channel = ctx.message.channel
        async for message in channel.history(before=ctx.message, limit=99):
            counter += 1
        await ctx.message.delete()
        counter += 1
        if counter == 100:
            await tmp.edit(content="There are now at least {} messages in {}".format(counter, channel.mention))
        elif counter == 1:
            await tmp.edit(content="There is now 1 message in {}".format(channel.mention))
        elif counter <= 99:
            await tmp.edit(content="There are now {} messages in {}".format(counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")

    @commands.command(aliases=["recents", "last"])
    async def recent(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.message.channel
        if not user:
            user = ctx.message.author
        quote = None
        async for message in channel.history(before=ctx.message, limit=100):
            if message.author == user:
                quote = message
                embed = discord.Embed(description=quote.content)
                embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
                embed.set_footer(text=(quote.created_at))
                await ctx.message.delete()
                await ctx.send(embed=embed)
                return
            if not quote:
                continue
            embed = discord.Embed(description="No message found")
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

def setup(bot):
    bot.add_cog(Count(bot))