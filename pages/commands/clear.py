import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount <= 0:
            embed = discord.Embed(description="Por favor, especifique um número maior que zero para limpar as mensagens.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        try:
            deleted = await ctx.channel.purge(limit=amount + 1)  # +1 para incluir o próprio comando
            embed = discord.Embed(description=f"{len(deleted) - 1} mensagem(s) foram apagadas.", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(description="Não tenho permissão para apagar mensagens neste canal.", color=discord.Color.red())
            await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="Você não tem permissão para gerenciar mensagens.", color=discord.Color.red())
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Clear(bot))
