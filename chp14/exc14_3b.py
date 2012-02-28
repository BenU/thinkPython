import anydbm
import pickle

bingoDB = anydbm.open('bingos.db', 'r')
bingoList = []
for letters, words in bingoDB.iteritems():
  lets = pickle.loads(letters)
  anas = pickle.loads(words)
  bingoList.append([len(anas), lets, anas])
  bingoList.sort(reverse=True)
for bingos in bingoList:
  print bingos
bingoDB.close()