"""rwge responses for given text inputs"""
import logging
import random

from asyncio import sleep

from .canned_phrases import canned_phrases
from .canned_phrases import random_unrelated_phrases
from .mother_jokes import mother_joke
from .config import PEOPLE_TO_ASK
from .config import DEFAULT_MOTHER_FREQUENCY

logger = logging.getLogger('rwge')


WAKE_UP_PHRASES = [
    'for the consistency of the peano axioms',
    'that i live in a universe with three spatial dimensions and one time dimension',
    'for the ratio between the strong and weak nuclear forces',
    'that i live in a euclidean universe',
    'that atoms exist',
]

settings = {
    'mother_likelihood': DEFAULT_MOTHER_FREQUENCY,
}


async def random_sleep():
    """rwge should wait a short random time before replying to any message"""
    await sleep(random.uniform(0, 2))


async def get_response(text, author, mentioned):
    """generate appropriate rwge response for the given message text

    :param text: str what was said in channel
    :param author: str author for message
    :param mentioned: bool whether rwge was named in this message
    :return:
    """
    await random_sleep()

    text = text.lower()
    if text.startswith('hello') and mentioned:
        response = f'hello {author}'
        return response

    random_value = random.randint(0, 200) / 2

    if mentioned:
        return direct_mentions_response(text)

    if 'how are you' in text:
        if random.randint(0, 1) == 0:
            return 'rubbish'
        await sleep(20)
        return 'that went badly'

    response = (
        check_canned_responses(random_value, text) or
        check_special_rules(random_value, text) or
        question_rules(random_value, text)
    )
    if response:
        return response

    logger.info("Nothing to respond to")


def question_rules(random_value, text):
    """Various options for replying to questions; may not respond though"""
    response = None

    if '?' not in text:
        response = None
    elif text.endswith('wii?'):
        response = "go on then"
    elif random_value < 43:
        response = "no"
    elif random_value < 50:
        response = "ask %s" % random.choice(PEOPLE_TO_ASK)
    elif random_value < 55:
        response = "it's non-quantifiable"
    elif random_value < 63:
        response = "seems reasonable"
    elif random_value < 70:
        response = "ok"

    return response


def check_canned_responses(random_value, text):
    """Check for responses based on simple trigger/response rules"""
    for triggers, blockers, probability, response in canned_phrases:
        if (
                all((trigger in text for trigger in triggers)) and
                all((blocker not in text for blocker in blockers)) and
                random_value <= probability
        ):
            return response

    for probability, response in random_unrelated_phrases:
        if probability == random_value:
            return response


def check_special_rules(random_value, text):
    """Some other behaviours that don't fit the easy trigger/response pattern"""
    if random_value < settings['mother_likelihood'] and len(text) < 200:
        if ': ' in text[:20]:
            text = text.split(': ', 1)[1]
        else:
            text = text
        return mother_joke(text)

    elif len(text) > 79 and random_value < 10:
        return "79 characters should be enough for anyone"
    elif 'thankful' in text:
        return 'i\'m thankful {}'.format(random.choice(WAKE_UP_PHRASES))
    elif 'grateful' in text:
        return 'i\'m grateful {}'.format(random.choice(WAKE_UP_PHRASES))
    elif ' 188 ' in text or text.endswith(' 188') or text.startswith('188 '):
        return 'the 188 is my favourite bus'


def direct_mentions_response(text):
    """If rwge was named directly, he has some different responses"""
    if "calm down" in text:
        return calm_down()
    elif "quiet" in text:
        return very_quiet()

    return default_reply(text)


def calm_down():
    """Behaviour for when rwge is told he's too loud"""
    settings['mother_likelihood'] -= 2
    return 'sorry'


def very_quiet():
    """Behaviour for when rwge is told he's too quiet"""
    settings['mother_likelihood'] += 2
    return 'sorry'


def default_reply(text):
    """Generate a response for mentions"""
    random_value = random.randint(0, 100)

    # catch any remaining questions
    if text[-1] == '?':
        response = random.choice([
            'no',
            'no',
            'maybe',
            'it\'s non-quantifiable',
            'seems reasonable',
            f'ask {random.choice(PEOPLE_TO_ASK)}',
        ])
        return response

    elif random_value < settings['mother_likelihood'] and len(text) < 200:
        if ': ' in text[:20]:
            text = text.split(': ', 1)[1]
        else:
            text = text

        result, new_text = mother_joke(text)
        new_text = new_text.strip('?')
        if result:
            return new_text

    if 20 < random_value <= 95:
        response = random.choice([
            "interesting",
            "seems reasonable",
            "rubbish",
            "i thought so",
            "good",
            "dubious",
            "fascinating",
            "shenanigans",
            "thanks",
        ])
        return response
