'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

import string

# Lists
the_list = [1,2,3,4,5]
beginning = 2
end = 4
index = 3
word = 'hannah'
sentence = "Mr. Owl ate my metal worm."
dictionnary = {"brand": "Ford", "model": "Mustang", "year": 1964}

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0], the_list[-1]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    new_list = the_list[beginning-1: end]
    new_list.reverse() 
    return new_list# hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    the_list[index] = the_list[index], the_list[index], the_list[index]
    return the_list

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    if word == word [::-1]:
        print("The word ", word, " is a palindrome!")
    else:
        print("The word ", word, " is not a palindrome!")
    return

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    nsentence = sentence.lower()
    nsentence = nsentence.replace(" ", "")
    nsentence = nsentence.translate(str.maketrans('', '', string.punctuation))
    if sentence == sentence [::-1]:
        print("The sentence: ", sentence, " is a palindrome!")
    else:
        print("The sentence: ", sentence, " is not a palindrome!")
    return

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2): 
    return


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    
    return

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    return
