from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import ModularBot

import logging

import discord
from discord.ext import commands
from discord.ext.commands import Context
from typing_extensions import Literal

from core.notifications import Notification

logger = logging.getLogger(__name__)


class Test(commands.Cog):
    def __init__(self, bot: "ModularBot") -> None:
        self.bot = bot

    @commands.hybrid_command(name="test")
    async def test(self, ctx: Context):
        embed = discord.Embed(description=self.bot.avatar_url)
        embed.set_author(name="Test", icon_url=self.bot.avatar_url)
        await ctx.send(embed=embed)
        raise discord.DiscordException("Test")

    @commands.hybrid_command(name="test-websocket")
    async def test2(
        self,
        ctx: Context,
        title: str,
        text: str,
        severity: Literal["error", "info", "success", "warning"],
    ):
        await self.bot.notification_queue.send(Notification(title, text, severity))

        await ctx.send("Sent notification")


async def setup(bot: "ModularBot"):
    await bot.add_cog(Test(bot))
