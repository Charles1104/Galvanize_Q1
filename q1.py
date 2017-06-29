import re
import string
import os
import sys
import operator
from decimal import *

#Helper function to remove all punctuations from a word or sentence "s"
def OnlyCharacter(s):
   return re.sub(r'[^\w\s]', '', s.lower())

#Helper function that will create a serie of a tuple of three words.
def phrases(words):
 phrase = []
 for word in words:
  phrase.append(word)
  if len(phrase) > 3:
   phrase.remove(phrase[0])
  if len(phrase) == 3:
   yield tuple(phrase)

def main():

   #list that will contain all the element of the text file. Split is done according to white spaces
   words_list = []
   with open(sys.argv[1], "r") as f:
    for line in f:
     words_list.extend(line.split())

   #For each element in our words_list, we apply the "OnlyCharacter" function. We then remove the empty elements from the list.
   new_words = map(OnlyCharacter, words_list)
   new_words = list(filter(None, new_words))

   print "Total word count:", len(new_words)

   #set will filter out the duplicates
   print "Unique words:", len(set(new_words))

   #count the number of sentences.
   nb_sentence = 0
   for word in words_list:
       if re.search(r'[.!?]', word):
           nb_sentence += 1

   print "Sentences:", nb_sentence

   #Average sentence length in words
   wordcounts = []
   with open(sys.argv[1], "r") as f:
    text = f.read()
    sentences = filter(None,re.split(r'[.!?]',text))

   for sentence in sentences:
    words = filter(None,sentence.split(' '))
    wordcounts.append(len(words))
   average_wordcount = Decimal(sum(wordcounts))/Decimal(len(wordcounts))

   print "Average words per sentence:", average_wordcount

   #List of words used in order of descending frequency
   my_dict = {}
   for item in new_words:
    my_dict[item] = new_words.count(item)
   sorted_my_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)

   print "Word counter", sorted_my_dict

   #Often used phrases (three or more words)
   repeated_phrases = []
   repeated_phrase_dic = {}

   for sentence in sentences:
    words = filter(None,sentence.split(' '))
    words = map(OnlyCharacter, words)
    repeated_phrases.append(list(phrases(words)))

   for phrase in repeated_phrases:
    for repeated_phrase in phrase:
      repeated_phrase_dic[repeated_phrase] = repeated_phrases.count(phrase)

   repeated_phrase_dic = dict([item for item in repeated_phrase_dic.iteritems() if item[1] > 2])

   print "Repeated phrase counter", repeated_phrase_dic


if __name__ == "__main__":
   main()