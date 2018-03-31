"""Generate "your mother" jokes by looking for common verbs"""
from .common_verbs import common_verbs


def mother_joke(sentence):
    """Generate "your mother" jokes by looking for common verbs"""
    words = [word.lower() for word in sentence.split(' ')]
    last_good_index = -1
    last_good_verb = ''

    # We find a verb to cut the sentence at, and put "your mother" before that verb.
    # Changing tense if necessary.
    for index, word in enumerate(words[:-1]):
        for alternative, verb in common_verbs.items():
            if word == alternative:
                last_good_index = index
                last_good_verb = verb

    # Didn't work out this time.
    if last_good_index == -1:
        return False, ''

    return joke_found(words, last_good_index, last_good_verb)


def joke_found(words, last_good_index, last_good_verb):
    """Having found a valid verb to split sentence on, turn it into a mother joke"""
    rest_of_joke = words[last_good_index + 1:]

    # I think finding a pronoun as the first word implies this is a question not a statement.
    # I'm inclined to try to mangle it into something better.
    # Another option is just return False for anything that appears to be a question.
    for pronoun in ['i', 'you', 'we', 'they', 'she', 'he', 'it']:
        if pronoun == rest_of_joke[0]:
            # return False, ''
            rest_of_joke = rest_of_joke[1:]

    flip_pronouns(rest_of_joke)
    change_pronouns_to_female(rest_of_joke)

    joke = (
        u"your mother{}{} {}"
        .format(
            u' ' if not last_good_verb.startswith("'") else u'',
            last_good_verb,
            u' '.join(rest_of_joke)
        )
    )

    # Throw away anything after the first punctuation.
    for punctuation in '.,;:?!"()<>@':
        joke = joke.split(punctuation)[0]
    joke = joke.strip()

    # Clean up pronoun/verb mismatch.
    common_pronoun_mismatches = [
        ('you was', 'you were'),
        ('i were', 'i was'),
        ('alot', 'a lot'),
    ]
    for mismatch in common_pronoun_mismatches:
        joke = joke.replace(*mismatch)

    # Other weirdness.
    if joke[-1] == "'":
        joke = joke[:-1]

    joke = joke.strip('?')

    return joke


def flip_pronouns(rest_of_joke):
    """Reverse the pronouns, usually makes more sense this way round"""
    for index, word in enumerate(rest_of_joke):
        if word == 'i':
            rest_of_joke[index] = 'you'
        # elif word == 'you':
        #    rest_of_joke[index] = 'i'
        elif word == 'your':
            rest_of_joke[index] = 'my'
        elif word == 'my':
            rest_of_joke[index] = 'your'
        elif word == 'yours':
            rest_of_joke[index] = 'mine'
        elif word == 'mine':
            rest_of_joke[index] = 'yours'


def change_pronouns_to_female(rest_of_joke):
    """Change self-referencing pronouns and possessives to female since subject is your mother"""
    for index, word in enumerate(rest_of_joke):
        if word == 'his':
            rest_of_joke[index] = 'her'
        elif word in ['we', 'they', 'he']:
            rest_of_joke[index] = 'she'
        elif word in ['myself', 'himself', 'yourself',
                      'themselves', 'yourselves', 'ourselves']:
            rest_of_joke[index] = 'herself'
        elif word in ["he's"]:
            rest_of_joke[index] = "she's"
        elif word in ["we've", "they've"]:
            rest_of_joke[index] = "she has"
