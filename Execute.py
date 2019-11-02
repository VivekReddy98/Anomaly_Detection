from Utils.GenerateGraphMatrices import GenerateGraphMatrices
from Utils.DeltaCon import DeltaCon
import scipy, math
from scipy import sparse
import numpy as np
import os, json
from copy import deepcopy
import sys, ast

def Parse(list_files):
	new = {}
	for file in list_files:
		line = file
		file = file.split("_")
		#common_string = "_".join(file[1:])
		file[0] = ''.join(["0" for i in range(0,3-len(file[0]))])+file[0]
		new["_".join(file)] = line
	return new

def GiveAffinity(EdgeFilePath, g, epsilon):
	G = GenerateGraphMatrices(g)
	I1, S1, A1, D1 = G.GenerateGraphObj(EdgeFilePath=EdgeFilePath)
	D = DeltaCon(epsilon)
	return D.ComputeAffinityMatrix(I1, D1, A1, S1)

def Similarity(AM1, AM2):
	AM1.data = np.sqrt(AM1.data)
	AM2.data = np.sqrt(AM2.data)
	Result = AM1-AM2
	d = np.sqrt(np.sum(np.square(Result.data)))
	return (1/(1+d))

def compute_similarity(list_files, dict_files, dataset, g, epsilon, results_dir):
	first_computed = False
	with open(results_dir+dataset+"/"+"time_series"+"_"+str(g)+"_"+str(round(epsilon,2))+".txt", "w+") as f:
		for i in range(0,len(list_files)-1):
			if not(first_computed):
				AM_old = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i]]), g=g, epsilon=epsilon)
				first_computed = True
			else:
				AM_old = AM_new
			AM_new = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i+1]]), g=g, epsilon=epsilon)
			sim_score = Similarity(AM_old, deepcopy(AM_new))
			f.write(str(sim_score))
			f.write("\n")
			print(dict_files[list_files[i]], dict_files[list_files[i+1]], round(sim_score,5))
	print("The scores have been documented")
	return None 

## Testing this class
if __name__ == '__main__':	
	data_dir = "/datasets/"
	results_dir = "results/"
	datasets = os.listdir(os.getcwd()+data_dir)
	with open("search_space_hyper_param.json") as f:
		hyper_param = json.load(f) 
	dataset = str(sys.argv[1])
	for param in ast.literal_eval(hyper_param[dataset]['node']):
		src_path = os.getcwd()+data_dir+dataset+"/"
		dict_files = Parse(os.listdir(src_path))
		list_files = list(dict_files.keys())
		list_files.sort()
		compute_similarity(list_files, dict_files, dataset, param[0], param[1], results_dir)

	
