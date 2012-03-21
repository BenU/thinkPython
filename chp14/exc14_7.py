import shelve
import imdb

def shelf_write(actor, date, title, role):
  # creates database with actor key and list of movies they were in
  title_str = title + ', ' + date
  d = shelve.open('actorMovies')
  if d.has_key(actor):
    currentMovieList = d[actor]
    currentMovieList.append(title_str)
    d[actor] = currentMovieList
  else:
    titleList = []
    titleList.append(title_str)
    d[actor] = titleList
  d.close()

  
def find_costars(fileName, newFileName='costars'):
	actorsMovies = shelve.open(fileName)
	moviesActors = shelve.open('movieActors')
	for actor, movieList in actorsMovies.iteritems():
		for movie in movieList:
			if moviesActors.has_key(movie):
				currentActorList = moviesActors[movie]
				if actor in currentActorList: break
				currentActorList.append(actor)
				moviesActors[movie] = currentActorList
			else:
				actorList = []
				actorList.append(actor)
				moviesActors[movie] = actorList
	actorsMovies.close()
	# at this point, db moviesActors has all the stars for each movie

	for movie, actorList in moviesActors.iteritems():
		coStarsDB = shelve.open(newFileName)
		for actor in actorList:
			actorIndex = actorList.index(actor)
			movieCoStars = actorList
			movieCoStars.remove(actor)
			if coStarsDB.has_key(actor):
				# attempt to add all movieCoStars to actors costarts in coStarsDB
				currentCostarList = coStarsDB[actor]
				for costar in movieCoStars:
					if costar not in currentCostarList: currentCostarList.append(costar)
				coStarsDB[actor] = currentCostarList			
			else:
				coStarsDB[actor] = movieCoStars
			actorList.insert(actorIndex, actor)
	coStarsDB.close()
	moviesActors.close()	

def shelf_print(fileName):
  print "in shelf_print"
  d = shelve.open(fileName)
  for k,v in d.iteritems():
    print k, v
  d.close()

# imdb.process_file('actors.list.gz', shelf_info)
imdb.process_file('actresses.list.gz', shelf_write, 10000)
find_costars('actorMovies')
shelf_print('costars')
# def process_file(filename, f, num=float('Inf')):