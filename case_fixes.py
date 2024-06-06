"""
file: case_fixes.py
author: Adam Islam
spell check case fixes for spellotron
"""
from helpers import *


def first_case_fix(word,wordbank,key):
    """
    Check for misspelling due to hitting an adjacent key. For each of the n letters, the
    program should try alternatives in the order they are listed in the key file. The first
    time a legal word is found this way, checking is done; return the fixed word.
    :param word:
    :param wordbank:
    :return:
    """
    for i in range(0,len(word)):
        for letter in key:
                new = swap_letter(word,letter,i)
                if check_for_word(new,wordbank)==True:
                    return new
    for i in range(0, (len(word))):
        lst = key[word[i]].strip().split(" ")
        for j in lst:
            new = swap_letter(word,j,i)
            if check_for_word(new,wordbank)==True:
                return new

def second_case_fix(word,wordbank):
    """
    An extra key was accidentally typed.
    Check for a misspelling due to failing to type one key.
    The first time a legal word is found this way, checking is done; return the fixed word.
    :return:
    """
    for i in range(0,len(word)):
        new = remove_letter(word,i)
        if check_for_word(new,wordbank)==True:
            return new

def third_case_fix(word,wordbank,key):
    """
    A key stroke was left out.
    Check for a misspelling due to typing an extra key.
    The first time a legal word is found this way, checking is done; return the fixed word.
    :return:
    """
    for letter in key:
        new = add_letter(word, letter, -1)
        if check_for_word(new, wordbank) == True:
            return new
    for i in range(0,len(word)):
        for letter in key:
            new = add_letter(word,letter,i)
            if check_for_word(new,wordbank)==True:
                return new
    for letter in key:
        new = add_letter(word, letter, len(word))
        if check_for_word(new, wordbank) == True:
            return new

def spell_check(word,wordbank,keys):
    """
    spell checks a word in the specified order, first case, second case, then third case
    """

    if word.isdigit():
        return word

    if first_case_fix(word,wordbank,keys)is not None:
        return first_case_fix(word,wordbank,keys)

    elif second_case_fix(word,wordbank) is not None:
        return second_case_fix(word,wordbank)

    elif third_case_fix(word,wordbank,keys) is not None:
        return third_case_fix(word,wordbank,keys)

    elif first_case_fix(word.lower(),wordbank,keys) is not None:
        return second_case_fix(word.lower(),wordbank)

    elif second_case_fix(word.lower(), wordbank) is not None:
        return second_case_fix(word.lower(), wordbank)

    elif third_case_fix(word.lower(), wordbank, keys) is not None:
        return third_case_fix(word.lower(), wordbank, keys)