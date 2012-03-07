import shelve
import imdb

def shelf_write(actor, date, title, role):
  # creates database with actor key and list of movies they were in
  title_str = title + ', ' + date
  d = shelve.open('actorMovies')
  if d.has_key(actor):
    print "actor already in dictionary!:", d[actor]
    currentMovieList = d[actor]
    currentMovieList.append(title_str)
    d[actor] = currentMovieList
  else:
    print "in else!"
    titleList = []
    titleList.append(title_str)
    d[actor] = titleList
  d.close()
  
def find_costars():
  # takes actorMovies and generates database with key[actor]: costars
  # this will be done in two steps
  # 1) create database with key[movie]: all actors
  # 2) for each actor in a given movie, add all the costars to costar db
  
  

def shelf_print(fileName):
  print "in shelf_print"
  d = shelve.open(fileName)
  for k,v in d.iteritems():
    print k, v
  d.close()

  
# imdb.process_file('actors.list.gz', shelf_info)
imdb.process_file('actresses.list.gz', shelf_write, 100)
shelf_print('actorMovies')
# def process_file(filename, f, num=float('Inf')):