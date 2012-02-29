import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html') 
for line in conn.fp:
  print line.strip()