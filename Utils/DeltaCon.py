import scipy, math
from scipy import sparse
import numpy as np
from pyspark import SparkContext, Row
from pyspark.sql import SQLContext
from pyspark.sql.functions import * 
from pyspark.sql.types import *
from graphframes import *
from random import shuffle
from Utils.GraphFrameGenerator import GraphFrameGenerator

class DeltaCon(): #GraphFrameGenerator
	def __init__(self): #SparkContextObj, SQLContextObj):
		#self.sc = SparkContextObj
		#self.sql = SQLContextObj
		#self.has_vertices_created = False
		pass

	def __getGroup(self, g, num_vertices):
		self.verticesGroup = {} 
		vertices = [i for i in range(0,num_vertices)]
		shuffle(vertices)
		if g>num_vertices:
			raise Exception("g cannot be greater than num_vertices")		
		chunk_size = int(math.ceil(num_vertices/g))
		#print(chunk_size)
		self.group_num = 0
		i = 0
		while self.group_num<g:
			if i+chunk_size<num_vertices:
				yield vertices[i:i+chunk_size]
				i = i+chunk_size
				self.verticesGroup[self.group_num] =  vertices[i:i+chunk_size]
				self.group_num = self.group_num+1
			else:
				yield vertices[i:num_vertices]
				self.verticesGroup[self.group_num] =  vertices[i:num_vertices]
				self.group_num = self.group_num+1
		yield None
		print("Thats all i have, hav fun")


	def GenSeedScoresMatrix(self, g, num_vertices):
		Ei = np.zeros((num_vertices, g))
		itr = self.__getGroup(g, num_vertices)
		list_vertices = next(itr)
		while list_vertices!=None:
			print(list_vertices, self.group_num)
			Ei[list_vertices,self.group_num] = 1
			list_vertices = next(itr)
		return sparse.csc_matrix(Ei)


## Testing this class
if __name__ == '__main__':
	#sc=SparkContext("local", "degree.py")
	#sqlContext = SQLContext(sc)
	#sqlContext.sql("set spark.sql.shuffle.partitions=2")
	#sc.setLogLevel("WARN")
	G = DeltaCon()
	print(G.GenSeedScoresMatrix(12, 12).todense())
 





