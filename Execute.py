from Utils.GenerateGraphMatrices import GenerateGraphMatrices
from Utils.DeltaCon import DeltaCon
import scipy, math
from scipy import sparse
import numpy as np
import os
from copy import deepcopy


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
	A1 = AM1.todense()
	A2 = AM2.todense()
	d = np.sqrt(np.sum(np.square(np.sqrt(A1)-np.sqrt(A2))))
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
			#AM_old = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i]]), g=g, epsilon=epsilon)
			AM_new = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i+1]]), g=g, epsilon=epsilon)
			sim_score = Similarity(AM_old, deepcopy(AM_new))
			f.write(str(sim_score))
			f.write("\n")
			print(dict_files[list_files[i]], np.sum(AM_old.data), dict_files[list_files[i+1]], np.sum(AM_new.data), sim_score)
	print("The scores have been documented")
	return None 

## Testing this class
if __name__ == '__main__':	
	data_dir = "/datasets/"
	results_dir = "results/"
	datasets = os.listdir(os.getcwd()+data_dir)
	g_epsilon = {'autonomous':[500,0.99], 'enron_by_day':[20,0.99],'p2p-Gnutella':[1000,0.99], 'voices':[20, 0.99]} 
	for dataset in datasets:
		src_path = os.getcwd()+data_dir+dataset+"/"
		dict_files = Parse(os.listdir(src_path))
		list_files = list(dict_files.keys())
		list_files.sort()
		#print(list_files)
		compute_similarity(list_files, dict_files, dataset, g_epsilon[dataset][0], g_epsilon[dataset][1], results_dir)

	
