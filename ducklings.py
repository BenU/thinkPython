prefixes = 'JKLMNOPQ'
suffix = 'ack'

duckling = ''

for letter in prefixes:
  duckling += letter
  if letter == 'Q' or letter == 'O':
    duckling += 'u'
  print duckling + suffix
  duckling = ''