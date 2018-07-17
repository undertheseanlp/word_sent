import re
import string
from .word_pattern import WordPatternFeature

PUNCTUATIONS = string.punctuation
DITGIT_PAT = re.compile('[-+]?\d+[\.\,]?\d*')
WORD_PATTERN = WordPatternFeature()


def contain_punct(word):
    for punct in PUNCTUATIONS:
        if punct in word and len(word) > 1:
            return True
    return False


def is_punct(word):
    result = False
    if word in PUNCTUATIONS:
        result = True
    return result


def contain_digit(word):
    for tok in word:
        if tok.isdigit():
            return True
    return False


def is_number(word):
    if DITGIT_PAT.match(word) is not None:
        return True
    return False


def get_pattern_for_word(word):
    return WORD_PATTERN.token_to_wordpattern(word)
