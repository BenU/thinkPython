from math import *
import sys

last_input = "nada"

while True:
  input = raw_input('Gimme some input to evaluate!: ')
  if input == 'done':
    print "Ok... bye!"
    print "Last input was %s" % last_input,
    print ", by the way..."
    break
  else:
    try:
      display = eval(input)
      last_input = display
      print display
    except SyntaxError:
      print "Oops!  Syntax Error."
    except:
      print "Unexpected errors:", sys.exc_info()[0]  
    
      

    
