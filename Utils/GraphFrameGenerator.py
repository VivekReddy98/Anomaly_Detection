from pyspark import SparkContext, Row
from pyspark.sql import SQLContext
from pyspark.sql.functions import * 
from pyspark.sql.types import *
from graphframes import *

# Class to handle importing/exporting data. Given an edge list, this returns a graphframes object
class GraphFrameGenerator():
	def __init__(self, SparkContextObj, SQLContextObj):
		self.sc = SparkContextObj
		self.sql = SQLContextObj
		self.has_vertices_created = False

	def __createVertices(self, count_vertices_edges):
		list_nodes = [i for i in range(0,int(count_vertices_edges[0]))]
		v_rdd = sc.parallelize(list_nodes)
		row_data = v_rdd.map(lambda l: Row(id=l))
		self.Vertices = self.sql.createDataFrame(row_data)
		return None

	# def __EdgeListName(self, timestamp_id):
	# 	if timestamp_id==None:
	# 		return "self.Edges"
	# 	return "self.Edges_" + str(timestamp_id)

	# def __GraphFrameName(self, timestamp_id):
	# 	if timestamp_id==None:
	# 		return "self.G"
	# 	return "self.G_" + str(timestamp_id)

	# def __createGraphFrame(self):
	# 	self.GF =
	# 	return None

	def __createEdges(self, delim=" "):
		lines = sc.textFile(self.EdgeFilePath)
		# Strip off header row.
		lines = lines.mapPartitionsWithIndex(lambda ind,it: iter(list(it)[1:]) if ind==0 else it)
		lines = lines.map(lambda l : l.strip().split(delim))
		row_data = lines.map(lambda l: Row(src=int(l[0]), dst=int(l[1])))
		self.Edges = self.sql.createDataFrame(row_data)
		return None


	def ReadFile(self, EdgeFilePath, delim=" ", **kwargs):
		self.EdgeFilePath = EdgeFilePath
		with open(self.EdgeFilePath,"r") as f:
			count_vertices_edges = f.readline().strip().split(" ")

		if not(self.has_vertices_created):
			self.__createVertices(count_vertices_edges)
			self.has_vertices_created = True

		self.__createEdges(delim=delim)
		return GraphFrame(self.Vertices,self.Edges)


## Testing this class
if __name__ == '__main__':
	sc=SparkContext("local", "degree.py")
	sqlContext = SQLContext(sc)
	sqlContext.sql("set spark.sql.shuffle.partitions=2")
	sc.setLogLevel("WARN")
	loadData = GraphFrameGenerator(sc, sqlContext)
	G = loadData.ReadFile("datasets/autonomous/0_autonomous.txt", delim=" ", edge_timestamp=True, timestamp_id=0)
	print("This graph has " + str(G.edges.count()) + " directed edges and " + str(G.vertices.count()) + " vertices.")
	print("You are good to go")





