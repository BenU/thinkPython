import os

def find_files(suffix, directory=None):
  if directory == None: directory = os.getcwd()
  foundFiles = []
  for root, dirs, files in os.walk(directory):
    for name in files:
      nameL = name.split('.')
      if (len(nameL) > 1) and (nameL[1] == suffix):
        path = os.path.join(root, name)
        print path
        foundFiles.append(path)
  return foundFiles
        
        
home = os.environ['HOME']
mp3s = find_files('mp3', home)
m4as = find_files('m4a', home)
musicFiles = mp3s + m4as
for mf in musicFiles:
  print mf
