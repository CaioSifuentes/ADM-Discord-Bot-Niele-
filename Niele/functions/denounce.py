import discord
from discord.ext import commands
from Niele_2.niele_main import niele_client


class DenounceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.slash_command()
    async def denunciar(self, ctx, user: discord.Member):
        reported_user = user.mention
        reported_user_name = user.name
        author_name = ctx.author.name
        author_mention = ctx.author.mention
        modal = Modal_Denuncia(title=f"Denunciar {reported_user_name}",
                               reported_user=reported_user,
                               author_name=author_name,
                               author_mention=author_mention)
        await ctx.send_modal(modal)


class Modal_Denuncia(discord.ui.Modal):
    def __init__(self, reported_user: str,
                 author_name: str,
                 author_mention: str,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.reported_user = reported_user
        self.author_name = author_name
        self.author_mention = author_mention
        self.add_item(discord.ui.InputText(label="Escreva o motivo da denuncia:", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):

        # Define os parâmetros da Embed, respectivamente: Denunciador, Denunciado e Motivo da Denuncia.
        embed = discord.Embed(title=f"Usuário Denunciado:", description=self.reported_user)
        embed.set_author(name=f'Reportado por {self.author_name} \n{self.author_mention}')
        embed.add_field(name="Motivo da denuncia:", value=self.children[0].value)

        report_channel = niele_client.get_channel(1080653770645577798)
        await interaction.response.send_message(f"Usuário {self.reported_user} denunciado."
                                                f"A denuncia será revisada pelos Supervisores adequados.", ephemeral=True)
        await report_channel.send(embeds=[embed])


def setup(bot: commands.Bot):
    bot.add_cog(DenounceCommands(bot))
