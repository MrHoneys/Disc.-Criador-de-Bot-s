import discord
from discord.ext import commands
import qrcode
import asyncio

class QRCode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qrcode(self, ctx, *, content: str):
        if content.startswith(("http://", "https://")):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(content)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Salvando o QR Code como arquivo temporário
            img_path = "temp_qr.png"
            img.save(img_path)

            # Deletando a mensagem do usuário
            await ctx.message.delete()

            # Enviando o QR Code no Discord
            with open(img_path, "rb") as file:
                sent_message = await ctx.send(file=discord.File(file))

            # Deletando o arquivo temporário após 3 minutos
            await asyncio.sleep(180)
            os.remove(img_path)

            # Deletando a mensagem do QR Code após 3 minutos
            await sent_message.delete()
        else:
            await ctx.send("Por favor, forneça uma URL válida para gerar o QR Code.")

def setup(bot):
    bot.add_cog(QRCode(bot))
