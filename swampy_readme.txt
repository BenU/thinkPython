sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/swampy-2.0')

At site: http://docs.python.org/tutorial/interpreter.html#the-interactive-startup-file
$ python
>>> import site
>>> site.getusersitepackages()
'/Users/benjaminunger/Library/Python/2.7/lib/python/site-packages'


# I created that director which didn't exist and added a file called "usercustomize.py"
# in that file I put:
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/swampy-2.0')


