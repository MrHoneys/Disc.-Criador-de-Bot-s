import discord
from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        
        embed = discord.Embed(title="Perfil do Usuário", color=member.color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Nome", value=member.display_name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Entrou no servidor", value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Conta criada em", value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        
        # Status
        embed.add_field(name="Status", value=member.status.name.capitalize(), inline=False)

        # Cargos
        roles = [role.mention for role in member.roles if role != ctx.guild.default_role]
        if roles:
            embed.add_field(name="Cargos", value=" ".join(roles), inline=False)
        
        # Atividade
        if member.activity is not None:
            if isinstance(member.activity, discord.Game):
                embed.add_field(name="Jogando", value=member.activity.name, inline=False)
            elif isinstance(member.activity, discord.Streaming):
                embed.add_field(name="Transmitindo", value=member.activity.name, inline=False)
            elif isinstance(member.activity, discord.Spotify):
                embed.add_field(name="Ouvindo Spotify", value=f"{member.activity.title} - {member.activity.artist}", inline=False)
            elif isinstance(member.activity, discord.CustomActivity):
                embed.add_field(name="Atividade Personalizada", value=member.activity.name, inline=False)

        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Profile(bot))
