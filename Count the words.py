# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:27:57 2019

@author: nsancheti
"""
#import the regular expressions library
import re
fhand = open('text file for python read.txt', 'r')
text = fhand.read()
words = re.split(r'[,.\s]\s*', text)

#create a dictionary to count the words
count_of_words = dict()

#figure out the most and least frequent words
most_frequent_word_frequency = 0
least_frequent_word_frequency = len(words)

for word in words:
    count_of_words[word] = count_of_words.get(word,0) + 1

#list down the most frequent word(s)
for word, count in count_of_words.items():
    if count == max(count_of_words.values()):
        print("Most frequent word", word, "occurred ", count, "times")
