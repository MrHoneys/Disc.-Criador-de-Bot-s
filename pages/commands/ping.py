import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong! 🏓", color=0x00ff00)
        embed.add_field(name="Latência do Bot", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        
        # Verifica se o autor do comando tem um avatar
        if ctx.author.avatar:
            embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        else:
            embed.set_footer(text=f"Solicitado por {ctx.author.display_name}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))
