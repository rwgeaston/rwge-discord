"""List of common verbs to make your mother jokes from"""
common_verbs_structured = {
    'is': [
        'am', 'are', 'be', 'were', 'was',
        "you're", "i'm"
    ],
    "'s": [
        "he's", "she's", "it's",
        "what's", "that's", "they're"
    ],
    "isn't": ["aren't", "weren't"],
    'has': ['have', 'had', "i'd", "you'd", "he'd", "she'd", "it'd", "that'd", "they'd"],
    "hasn't": ["haven't", "hadn't"],
    'does': ['did', 'do'],
    "doesn't": ["didn't", "don't"],
    'says': ['said', 'say'],
    'gets': ['get', 'got'],
    'makes': ['made', 'make'],
    'goes': ['went', 'goes'],
    'knows': ['know', 'knew'],
    'takes': ['take', 'took'],
    'sees': ['see', 'saw'],
    'comes': ['come', 'came'],
    'thinks': ['think', 'thought'],
    'looks': ['look', 'looked'],
    'wants': ['want', 'wanted'],
    'gives': ['give', 'gave'],
    'uses': ['use', 'used'],
    'finds': ['find', 'found'],
    'tells': ['tell', 'told'],
    'asks': ['ask', 'asked'],
    'works': ['work', 'worked'],
    'seems': ['seem', 'seemed'],
    'feels': ['feel', 'felt'],
    'tries': ['try', 'tried'],
    'leaves': ['leave', 'left'],
    'calls': ['call', 'called'],
    'plays': ['play', 'played'],
    'hopes': ['hope', 'hoped'],
    'buys': ['buy', 'bought'],
    'stops': ['stop', 'stopped'],
    'tests': ['test', 'tested'],
    'smacks': ['smack', 'smacked'],
    'strikes': ['strike', 'striked'],
    'enjoys': ['enjoy', 'enjoyed'],
    'beats': ['beat'],
    'adds': ['add', 'added'],
    'removes': ['remove', 'removed'],
}


def flatten_list():
    """Structure above is human readable but not very efficient"""
    flattened = {}
    for verb, alternative_tenses in common_verbs_structured.items():
        flattened[verb] = verb
        for alternative_tense in alternative_tenses:
            flattened[alternative_tense] = verb
    return flattened


common_verbs = flatten_list()
