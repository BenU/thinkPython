actors = ['tom', 'dick', 'harry', 'sally']
for actor in actors:
	costars = actors
	actorIndex = actors.index(actor)
	costars.remove(actor)
	print actor, costars
	actors.insert(actorIndex, actor)
	
