import scipy, math
from scipy import sparse
import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from scipy.sparse.linalg import spsolve
from Utils.GenerateGraphMatrices import GenerateGraphMatrices

class DeltaCon():
	def __init__(self, epsilon):
		self.epsilon = epsilon 

	def ComputeAffinityMatrix(self, I, D, A, S):
		D.data = D.data*(self.epsilon**2)
		A.data = A.data*self.epsilon
		Left_operand = I + D - A
		AffinityMatrix = spsolve(Left_operand, S)
		print("Affinity Matrix Computed :)")
		return AffinityMatrix





