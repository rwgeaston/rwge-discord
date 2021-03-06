"""Define discord.py handlers and run client loop"""
import logging

import discord

from .config import ALLOWED_CHANNELS
from .rwge import get_response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('rwge')

client = discord.Client()


@client.event
async def on_message(message):
    """Check if this is an appropriate message to reply to and then generate a reply
    :param message: message object from discord.py library
    :return: None; will have side effects if appropriate
    """
    if message.author == client.user:
        logger.info('No point replying to myself')
        return

    mentioned = any((client.user.id == mention.id for mention in message.mentions))
    if mentioned:
        logger.info("I was mentioned")

    if message.channel.is_private:
        logger.info(f'Can respond to private message')
    elif message.channel.name in ALLOWED_CHANNELS:
        logger.info(f'{message.channel} is an allowed channel to respond')
    else:
        logger.info(f'{message.channel} is not my channel')
        return

    try:
        response = await get_response(message.content, message.author.name, mentioned)
    except Exception as e:  # it's more useful to just log every failure here # pylint: disable=broad-except
        response = None
        logger.exception(e)
        logger.warning(f'Had an exception when replying to message "{message.content}" in {message.channel}')

    if response:
        logger.info(f'Replying to message "{message.content}" in {message.channel} with: "{response}"')
        await client.send_message(message.channel, response)


@client.event
async def on_ready():
    """Shows some debug on startup"""
    logger.info(f'Logged in as {client.user.name} (ID: {client.user.id})')
