import random

#################################################################################################
#                                      Auxiliar functions                                       #
#################################################################################################


def makelink(graph,nodeA,nodeB):
	if nodeA not in graph:
		graph[nodeA] = [None,{}]
	(graph[nodeA][1])[nodeB] = 'actived'
	if nodeB not in graph:
		graph[nodeB] = [None,{}]
	(graph[nodeB][1])[nodeA] = 'actived'

	return graph 

def setbroadcastmessage(graph,x):
	print "Set broadcast message: "
	print x
	print graph[x][1].keys()
	print "\n"

	neighbours = graph[x][1].keys()

	for i in neighbours:
		graph[i][0].getMessage(graph[x][0].exportMessage())

	return graph

def destructnodes(graph,node_):
	print "Destruct nodes: "
	if graph[node_][0].value <= 0:
		print "Nodos vecinos a destruir"
		print graph[node_][1].keys()
		print "\n"
		neighbours = graph[node_][1].keys()
		for n in neighbours:
			del(graph[n][1][node_])
		del(graph[node_])
		print "Nodo destruido ..."
		print node_
		print "\n"

	return graph

#################################################################################################
#                                          Main functions                                       #
#################################################################################################

class Node:
	def __init__(self,posx,posy):
		self.x = posx
		self.y = posy
		self.value = 1000

	def getMessage(self,val):
		self.value += val

	def exportMessage(self):
		return random.randint(-1000,200)

def graph_initial():
	graph_test = {}
	n = 3
	count = 0
	# Se crea el primer nodo: [instancia, links con otros nodos]
	graph_test[0] = [Node(0,0),{}]

	for i in range(1,n*n):
		if i < n:
			graph_test[i] = [Node(i,0),{}]
			makelink(graph_test,i,i-1)
		else:
			graph_test[i] = [Node(int(i%n),int(i/n)),{}]
			makelink(graph_test,i, i - 1) # Link horizontal
			makelink(graph_test,i,i - n) # Link vertical

		if (i+1) == n:
			count += 1

	return graph_test,i


def main_test():
	graph_t,n = graph_initial()
	count = 0

	while True:
		graph_t[n] = [Node(int(n%3),int(n/3)),{}]
		makelink(graph_t,n, n - 1) # Link horizontal
		makelink(graph_t,n,n - 3) # Link vertical

		i = 0
		j = 0

		while i < len(graph_t):
			if i in graph_t:
				setbroadcastmessage(graph_t,i)
		 	i+=1

		while j < len(graph_t):
			if j in graph_t:
				destructnodes(graph_t,j)
			j+=1		

		print count
		print graph_t

		if len(graph_t) <= 0:
			return "Sustentabilidad no lograda..." , count

		count += 1
		n += 1



#main_test()



