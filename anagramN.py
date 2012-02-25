# create dictionary of all letter combinations (in alphabetical order) and the anagrams they can make
from bisect import *

words = []
fin = open('words.txt')
for line in fin:
  word = line.strip()
  words.append(word)
fin.close()

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
      return i
    else:
      return -1

letterCombose = []
aDict = {}
for word in words:
  letters = []
  for letter in word:
    letters.append(letter)
    letters.sort()
    lettersTup = tuple(letters)
  if index(letterCombose, lettersTup) != -1:
    aDict[lettersTup] = aDict[lettersTup] + [word]
  else: # doesn't yet exist
    insort_left(letterCombose, lettersTup)
    aDict[lettersTup] = [word]

def sort_dict(ad):
  anaList = []
  for letters, words in ad.iteritems():
    anaList.append([len(words), letters, words])
  anaList.sort(reverse=True)
  for anagrams in anaList:
    if len(anagrams[1]) == 8: print anagrams
    
  

anaDict = {}
for letters, words in aDict.iteritems():
  if len(words) > 1:
    anaDict[letters] = words

sort_dict(anaDict)