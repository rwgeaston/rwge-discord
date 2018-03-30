"""rwge responses for given text inputs"""
import logging

logger = logging.getLogger('rwge')


async def get_response(text, author, mentioned):
    """generate appropriate rwge response for the given message text

    :param text: str what was said in channel
    :param author: str author for message
    :param mentioned: bool whether rwge was named in this message
    :return:
    """
    if text.startswith('hello') and mentioned:
        response = f'hello {author}'
        return response

    logger.info("Nothing to respond to")
