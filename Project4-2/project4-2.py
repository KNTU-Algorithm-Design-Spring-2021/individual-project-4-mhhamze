from collections import defaultdict
class Graph:

	def __init__(self,graph):
		self.graph = graph
		self. ROW = len(graph)
		
	def BFS(self,s, t, parent):
		visited =[False]*(self.ROW)
		queue=[]
		queue.append(s)
		visited[s] = True
		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
		print(parent)
		return True if visited[t] else False
			

	def findDisjointPaths(self, start, end):
		parent = [-1]*(self.ROW)
		max_flow = 0 
		while self.BFS(start, end, parent) :
			path_flow = float("Inf")
			s = end
			while(s != start):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]
			max_flow += path_flow
			v = end
			while(v != start):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow


if __name__ == "__main__":   
	graph = [[0, 1, 1, 1, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0, 0, 0, 1],
		[0, 1, 0, 0, 1, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0]]

	g = Graph(graph)
	start = 0
	end = 7
	print ("There can be maximum %d edge-disjoint paths from %d to %d" %
			(g.findDisjointPaths(start, end), start, end))
