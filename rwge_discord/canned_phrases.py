"""Static text triggers and responses"""

canned_phrases = [
    (('graph theory',), (), 100, 'far too easy'),
    (('string theory',), (), 100, 'complete rubbish'),
    (('dutch',), (), 85, 'the netherlands don\'t exist'),
    (('holland',), (), 85, 'the netherlands don\'t exist'),
    (('netherlands',), (), 85, 'the netherlands don\'t exist'),
    (('maths',), (), 50, 'too complicated'),
    (('asuffiel',), (), 10, 'asuffiel is wrong'),
    (('ts mode',), (), 100, 'rm mode is the best'),
    (('oooo, not rm mode!',), (), 100, 'rm mode is the best'),
    (('mode', 'the best'), (), 100, 'response'),
    (('syntax error',), (), 90, 'your mother is a syntax error'),
    (('train', 'ealing'), (), 5, 'your mother is a train to ealing'),
    (('statistics',), (), 80, 'boring'),
    (('math',), ('appli',), 80, 'too easy'),  # Note order of these two crucial
    (('math',), ('appli',), 90, 'trivial'),
    ((' short ',), ('too long',), 50, '80 characters should be enough for anyone'),
    ((' long ',), ('too long',), 50, '80 characters should be enough for anyone'),
    (('liquid',), (), 95, 'i don\'t understand the physics of liquid at all'),
    (('physics',), (), 95, 'i don\'t understand the physics of liquid at all'),
    (('poker',), (), 55, 'slacker'),
    ((' 188 ',), (), 100, 'the 188 is my favourite bus'),
    (('ds mode',), (), 100, 'it\'s called rm mode'),
    (('brown sauce',), (), 100, 'i like brown sauce'),
    (('spoons',), (), 100, 'i love spoons'),
    (('estate',), (), 100, 'i\'m sick of estate agents'),
]

random_unrelated_phrases = [
    (98.5, 'that went badly'),
    (99, 'dubious'),
    (99.5, 'don\'t do that')
]
