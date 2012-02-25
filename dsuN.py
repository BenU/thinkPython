from random import shuffle
testList = ['cat', 'dog', 'coffee', 'zebra', 'ostritch', "monkey", "mouse", "mickey", "elephant"]
print testList
shuffle(testList)
print testList




def sort_by_length(words):
  t = []
  for word in words:
    t.append((len(word), word))
  
  # at this point we've got list, t, of tuples with 
  # first element = length.
  
  t.sort(reverse=True)
  # now we've got List, t, sorted by length with ties broken by reverse, alphabetical order
  
"""  
  length = 0
  temp_t = []
  for length, word in t:
    if len(temp_t) == 0:
      temp_t.append((length, word))
    elif length > temp_t[0][0]:
      temp_t.append((length, word),0)
    elif length < temp_t[len(temp_t-1)][0]:
      temp_t.append((length, word))
    else:  # the length of word is somewhere in the middle
      count = 0
      while length <= temp_t[count][0]:
        if count == len(temp_t)-1: break
        count += 1
      
  # if word longer than first word, put at beginning
  # if word shorter than last word, put at the end
  # else traverse until between
  # if length is equal, generate randome bit(0 or 1) and
  # place word before or after depending on result
    
  t.sort(reverse=True)
  
  res = []
  for length, word in t:
    res.append(word)
  return res
  
testList = ['cat', 'dog', 'coffee', 'zebra', 'ostritch', "monkey", "mouse", "mickey", "elephant"]
print sort_by_length(testList)
"""