import asyncio
import json
import logging
import os

from redbot.core import commands
from redbot.core import Config
import rgr

logger = logging.getLogger(__name__)

class RGR (commands.Cog):
        
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=15646486532)
        self.config.register_global(listen_channels={})
    
    # Parse !rgr verbiage
    @commands.command(aliases=["r", "roll", "dice"], pass_context=True, rest_is_raw=True, description='Rolls dice. Uses an in development domain specific language.')
    @asyncio.coroutine
    async def rgr(self, ctx, *roll : str):
        try:
            # discord.py parses arguments for us, we can't have that.
            expr = " ".join(roll)
            logger.debug(expr)
            _, response, _ = rgr.roll(expr)
            await ctx.send("{} rolls {}".format(ctx.message.author, response))
        except Exception as err:
            logger.warn(err)
            await ctx.send("Could not complete {}'s roll:\n{}".format(ctx.message.author, err))
    
    @commands.command(aliases=["rollChannel", "autoRoll"], pass_context=True, rest_is_raw=True, description='Sets the current channel roll status')
    @asyncio.coroutine
    async def set_auto_roll(self, ctx, enabled: bool=True):
        async with self.config.listen_channels() as lc:
            lc[ctx.message.channel.id] = enabled
    
    @asyncio.coroutine
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        cid = str(message.channel.id)
        async with self.config.listen_channels() as lc:
            if (cid not in lc) or (not lc[cid]):
                return
        try:
            logger.debug("Rolling: %s", message.content)
            _, response, _ = rgr.roll(message.content)
            await message.channel.send(  "{} rol {}".format(message.author, response))
        except Exception as e:
            logger.debug("Problem while rolling: %s",e)


def setup(bot):
    cog = RGR(bot)
    bot.add_cog(cog)
    #bot.add_listener(cog.on_message)
