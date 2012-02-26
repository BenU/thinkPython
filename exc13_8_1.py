# arguments: word(with puntuation) and prefixLen=2
# from text file collect prefixLen words with punctuation.
# put prefix in dictionary
# [prefix]: [suffix, number of appearances]
# use exc13_7 to choose random words

import string

def process_file(filename, prefixLen=2):
  h = dict()
  fp = open(filename)
  for line in fp:
    process_line(line, prefixLen, h)
  return h
  
def process_line(line, prefixLen, h):
  # line = line.replace('-', ' ') # leaving out since looking for randome stuff
  
  for word in line.split():
    word = word.strip(string.whitespace)
    # word = word.lower()
    
    
    
    