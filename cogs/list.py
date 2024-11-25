import discord
from discord.ext import commands

class CommandList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="help-command", description="Lemon Botが提供するすべてのコマンドを表示します。")
    async def command_list(self, interaction: discord.Interaction):
        """Botが提供するすべてのコマンドとその説明を表示"""
        embed = discord.Embed(title="Lemon Botのコマンド一覧", description="以下はLemon Botが提供するコマンドとその説明です。", color=discord.Color.green())

        # コマンド一覧の取得
        for command in self.bot.tree.get_commands():
            # コマンド名と説明を埋め込む
            embed.add_field(name=f"/{command.name}", value=command.description if command.description else "説明なし", inline=False)

        await interaction.response.send_message(embed=embed)

# Cogのセットアップ
async def setup(bot):
    await bot.add_cog(CommandList(bot))
