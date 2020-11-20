import discord
from discord.ext import commands
import settings


class NotImplementedError(Exception):
    pass


class Discord(discord.Client):
    async def on_ready(self):
        message = self.create_message(self.provider, self.link)
        if settings.DISCORD_SEND_CHANNEL:
            for guild in self.guilds:
                if guild.id == settings.DISCORD_GUILD_ID:
                    self.guild = guild
            for channel in self.guild.text_channels:
                if channel.id == settings.DISCORD_CHANNEL_ID:
                    self.channel = channel
            await self.channel.send(message)
        if settings.DISCORD_SEND_DM:
            user = await self.fetch_user(settings.DISCORD_USER)
            await user.send(message)


class Email:
    def alert_email(self, message):
        raise NotImplementedError


class Text:
    def alert_text(self, message):
        raise NotImplementedError


class Alert(Discord, Email, Text):
    def __init__(self, *args, **kwargs):
        self.provider = kwargs.pop('provider')
        self.link = kwargs.pop('link')
        super().__init__()

    def create_message(self, provider=None, link=None):
        return f'Stock available at {provider}, more info here: {link}'

    async def alert(self):
        if settings.SEND_DISCORD:
            await self.start(settings.DISCORD_TOKEN)
        if settings.SEND_EMAIL:
            self.alert_email()
        if settings.SEND_TEXT:
            self.alert_text()


