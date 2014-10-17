string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""

def count_unique(string1, words):

    distinct_words={} 

    for entry in words: #for each list item in the list
        word_count=distinct_words.get(entry, 0) +1 #add entry to dictionary for word 
        #and its word count -start at 1 for new words, otherwise add 1 to the value already in the dictionary
        distinct_words[entry]=word_count #the dictionary value for the word is its word count, this adds key/value pair  
  
    print "This is a dictionary of distinct words and how often they occur: %r" % distinct_words

count_unique(string1, words)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):

    new_set=set(list1)
    another_set=set(list2)

    # print new_set
    # print another_set

    print "These are the numbers these sets do have in common"
    common_elements = new_set.intersection(another_set)
    print common_elements

    # print "These are the numbers these two sets do not have in common"
    # uncommon_elements = new_set ^ another_set
    # print uncommon_elements

    # number_counter = []

    # for numbers in list2:
    #     if numbers in list1:
    #         number_counter.append(numbers)

    # print number_counter

common_items(list1, list2)
"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    
    numbers = {}

    for entry in numbers:
        numbers[entry]=numbers.get(list1[entry], list2[entry])

    print "Here are two lists combined into a dictionary %r" % numbers

common_items2(list1, list2)
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    pass

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""