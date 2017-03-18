from discord.ext import commands
import inspect
import BotIDs

class Eval():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eval(self, ctx, *, code : str):
        if not ctx.author.id == BotIDs.dev_id:
            return

        else:
            original = ctx.message

            code = code.strip("` ")
            python = "{}"
            result = None

            env = {
                "bot": self.bot,
                "ctx": ctx,
                "message": ctx.message,
                "guild": ctx.message.guild,
                "channel": ctx.message.channel,
                "author": ctx.message.author
            }

            env.update(globals())

            try:
                result = eval(code, env)
                if inspect.isawaitable(result):
                    result = await result
            except Exception as e:
                await ctx.channel.send(python.format(type(e).__name__ + ": " + str(e)))
                await ctx.message.delete()
                return

            lines = ["```py"]
            lines.append(f">>> {code}")
            lines.append(">>> {}".format(python.format(result)))
            lines.append("```")

            await original.edit(content="\n".join(lines))

def setup(bot):
    bot.add_cog(Eval(bot))