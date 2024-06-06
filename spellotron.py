"""
file: spellotron.py
author: Adam Islam
spell-checks a text
"""
from case_fixes import *
import sys

KEY_ADJACENCY_FILE = create_dict("keyboard_letters.txt")

LEGAL_WORD_FILE = create_set("american_english.txt")

PUNCTUATION_SET = {"_", "-" "[","]","[","]", "{","}","(",")","@","#","^","&",".","!","?",":",";","'",'"',"*","+","=","/"}

def read_words(filename):
    """
    creates a list of words in the file, including punctuation
    :param filename:
    :return:
    """

    a=[]
    with open(filename) as b:
        for i in b:
            for j in i.split():
                a.append(j)
    return a

def words_mode(text):
    """
    runs the spellotron in words mode
    :param text: text input
    """
    word_count = 0
    print()
    og_words = []
    corrected_words = []
    unknowns = []

    for lne in text:
        lne = lne.split()
        for i in range(0, len(lne)):
                front,word,back = remove_punctuation(lne[i])
                if check_for_word(word, LEGAL_WORD_FILE) == False:
                    a = spell_check(word, LEGAL_WORD_FILE, KEY_ADJACENCY_FILE)
                    if a is None:
                        unknowns.append(front+word+back)
                    else:
                        og_words.append(front+a+back)
                        corrected_words.append(front+word+back)
                word_count+=1
    for i in range(0,len(corrected_words)):
        print(str(corrected_words[i])+"->"+str(og_words[i]))
    corrected_words.sort()
    unknowns.sort()
    print()
    print(str(word_count) + " words read from file.")
    print()
    print(str(len(corrected_words)) + " Corrected Words")
    print(corrected_words)
    print()
    print(str(len(unknowns)) + " Unknown Words")
    print(unknowns)
    print()

def lines_mode(text):
    """
    runs spellotron in lines mode
    :param text: input text
    """
    word_count = 0
    print()
    corrected_words = []
    unknowns = []
    new = []
    new_text = []
    line = ""
    for lne in text:
        lne = lne.split()
        for i in range(0, len(lne)):
            for j in lne[i].split():
                front,word,back = remove_punctuation(j)
                if check_for_word(word, LEGAL_WORD_FILE) == False:
                    a = spell_check(j, LEGAL_WORD_FILE, KEY_ADJACENCY_FILE)
                    if a is None:
                        line = line + word + " "
                        unknowns.append(front + word + back)
                    else:
                        line = line+str(a)+ " "
                        corrected_words.append(front + word + back)
                else:
                    line = line + j+" "
                word_count += 1
            new_text.append(line)

        line+="\n"

    print(line)
    corrected_words.sort()
    unknowns.sort()
    print()
    print(str(word_count)+" words read from file.")
    print()
    print(str(len(corrected_words)) + " Corrected Words")
    print(corrected_words)
    print()
    print(str(len(unknowns)) + " Unknown Words")
    print(unknowns)
    print()


def remove_punctuation(word):
    """
    removes the beginning and ending punctuation of a word, returns the front, back and word itself
    """
    front = ""
    back = ""
    while word[0] in PUNCTUATION_SET:
        front = front+word[0]
        word = word[1:]
    while word[-1] in PUNCTUATION_SET:
        back = back+word[-1]
        word = word[:len(word)-1]
    return front,word,back

def main():
    if len(sys.argv)<2:
        raise IndexError("Not enough parameters")
    elif len(sys.argv)==2:
        if sys.argv[1]=="words":
            words_mode(sys.stdin)
        elif sys.argv[1]=="lines":
            lines_mode(sys.stdin)
        else:
            raise IndexError("Must Enter words or lines")
    elif len(sys.argv)==3:
        if sys.argv[1]=="words":
            words_mode(open(sys.argv[2]))
        elif sys.argv[1]=="lines":
            lines_mode(open(sys.argv[2]))

main()
