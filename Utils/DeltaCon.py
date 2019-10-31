import scipy, math
from scipy import sparse
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import pairwise_distances 
from random import shuffle
from scipy.spatial.distance import cdist
from scipy.sparse.linalg import inv
import time
from Utils.GenerateGraphMatrices import GenerateGraphMatrices

class DeltaCon():
	def __init__(self, epsilon):
		self.epsilon = epsilon 

	def ComputeAffinityMatrix(self, I, D, A, S):
		D.data = D.data*(self.epsilon**2)
		A.data = A.data*self.epsilon
		Left_operand = I + D - A
		Left_operand_inv = inv(Left_operand)
		AffinityMatrix = Left_operand_inv.dot(S)
		return AffinityMatrix

def RootED(AM1, AM2):
	AM1.data = np.sqrt(AM1.data)
	AM2.data = np.sqrt(AM2.data)
	Result = AM1-AM2
	d = np.sqrt(np.sum(np.square(Result.data)))
	return d

def Similarity(d):
	return (1/(1+d))

## Testing this class
if __name__ == '__main__':
	Delta = DeltaCon(0.5)
	
	start = time.time()
	G = GenerateGraphMatrices(30)
	I1, S1, A1, D1 = G.GenerateGraphObj(EdgeFilePath="datasets/autonomous/1_autonomous.txt")
	AM1 = Delta.ComputeAffinityMatrix(I1, D1, A1, S1)
	print((time.time()-start))



	G = GenerateGraphMatrices(30)
	I2, S2, A2, D2 = G.GenerateGraphObj(EdgeFilePath="datasets/autonomous/2_autonomous.txt")
	AM2 = Delta.ComputeAffinityMatrix(I2, D2, A2, S2)

	print(np.sum(A1), np.sum(A2), np.sum(D1), np.sum(D2), np.sum(AM1), np.sum(AM2))

	print(Similarity(RootED(AM1,AM2)))





