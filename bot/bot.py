import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, prefix, token, ban_service):
        super().__init__(command_prefix=prefix)
        self.token = token
        self.ban_service = ban_service

    async def on_ready(self):
        print('Bot is ready.')

    async def on_member_join(self, member):
        await self.ban_service.ban_if_banned(member)
