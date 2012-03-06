# I'm abandoning this exercise.  For some reason, os.popen() can't find some of the files and directories.  I\'m not sure
# why.  Tracking down that bug in my or os.popen()\'s code is taking too long.  I've created checkSum's for many files,
# am confident I could avoid duplicates but that bug is taking too long to track down.  I continue...

import os

noFileCount = 0

def find_files(suffix, directory=None):
  if directory == None: directory = os.getcwd()
  foundFiles = []
  for root, dirs, files in os.walk(directory):
    for name in files:
      nameL = name.split('.')
      if (len(nameL) > 1) and (nameL[-1] == suffix):
        path = os.path.join(root, name)
        # print path
        foundFiles.append(path)
  return foundFiles
  
def creatCheckSum(fileName):
	print "In creatCheckSum!"
	cmd = "openssl md5 < " + fileName
	print "cmd = ", cmd
	try:
		fp = os.popen(cmd, 'r')
	except:
		return -1
	try:
		checkSum = fp.read()
	except: 
		return -2
	try:
		fp.close()
	except:
		return -3
	return checkSum

        
musicDict = {}        
home = os.environ['HOME']
mp3s = find_files('mp3', home)
m4as = find_files('m4a', home)
musicFiles = mp3s + m4as
for mf in musicFiles:
	checkSum = creatCheckSum(mf)
	if checkSum == "": break
	if checkSum in musicDict.values():
		print "Duplicate:", mf
	else:
		musicDict[mf] = checkSum

for k,v in musicDict:
	print k
	print v
	print


  
  