"""
file: helpers.py
author: Adam Islam
helper functions for spellotron
"""

def create_dict(filename):
    """
    creates a dictionary from a file
    """
    dict1 = dict()
    lst = read_file(filename)
    for i in lst:
        dict1[i[0]] = i[1:]
    return dict1

def create_set(filename):
    """
        creates a set from a file
        """
    a = set()
    lst = read_file(filename)
    for i in lst:
        a.add(i)
    return a


def read_file(filename):
    """
    changes file into a list with each index as a line in the file
    :param file: name of file to be turned into an array
    :return:
    """
    a = []
    with open(filename) as b:
        line = b.readline().strip()
        while line != "":
            a += [(line)]
            line = b.readline().strip()
    return (a)

def make_list_from_str(word):
    """
    turns a string into a list of each letter
    :param word:
    :return:
    """
    lst=[]
    for i in word:
        lst.append(i)
    return lst

def remove_letter(word,index):
    """
    removes a letter from an index in a word
    """
    original = make_list_from_str(word)
    copy = []
    for i in range(0,len(original)):
        if i == index:
            original = remove_from_list(original, i)
            new = "".join(original)
    return new

def add_letter(word,letter,index):
    """
        adds a letter from an index in a word
        """
    original = make_list_from_str(word)
    copy = []
    for i in range(0, len(original)):
        if i == index:
            original.insert(index,letter)
            new = "".join(original)
    if index == -1:
        original.insert(0, letter)
        new = "".join(original)
    if index==len(word):
        original.append(letter)
        new = "".join(original)
    return new

def remove_from_list(lst,index):
    """
        removes a object from an list
    """
    new = []
    counter = 0
    for i in lst:
        if counter != index:
            new.append(i)
        counter+=1
    return new

def check_for_word(word,wordbank):
    """
        checks to see if a word is in the dictionary
    """
    for i in wordbank:
        if word in wordbank:
            return True
        else:
            return False

def swap_letter(string,letter,index):
    """
    puts a new letter in the index of a string
    """
    string = remove_letter(string,index)
    new = add_letter(string,letter,index)
    return new


