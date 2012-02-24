

def do_twice(f, arg):
	f(arg)
	f(arg)
	
def print_word(word):
	print word
	
def do_four(f,arg):
	do_twice(f, arg)
	do_twice(f, arg)
	
	
do_twice(print_word, 'spam')
do_four(print_word, "eggs 'n ham ")