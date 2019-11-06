from Utils.GenerateGraphMatrices import GenerateGraphMatrices
from Utils.DeltaCon import DeltaCon
import scipy, math
from scipy import sparse
import numpy as np
import os, json
from copy import deepcopy
import sys, ast, time

def Moving_Range_Mean(lis):
    l = lis.shape[0]
    arr = lis - np.roll(lis, -1)
    return np.nansum(np.absolute(arr[1:-1]))/(l-1)

def give_stats(lis):
    mean_ = Moving_Range_Mean(lis)
    median_ = np.nanmedian(lis)
    upper_t = median_ + 3*mean_
    lower_t = median_ - 3*mean_
    return mean_, median_, lower_t, upper_t

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
	AM1.data = np.sqrt(AM1.data.clip(0))
	AM2.data = np.sqrt(AM2.data.clip(0))
	Result = AM1-AM2
	d = np.sqrt(np.sum(np.square(Result.data)))
	return (1/(1+d))

def compute_similarity(list_files, dict_files, dataset, g, epsilon, results_dir):
	first_computed = False
	with open(results_dir+dataset+"/"+"time_series"+"_"+str(g)+"_"+str(round(epsilon,2))+".txt", "w+") as f:
		for i in range(0,len(list_files)-1):
			start = time.time()
			if not(first_computed):
				AM_old = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i]]), g=g, epsilon=epsilon)
				first_computed = True
			else:
				AM_old = AM_new
			AM_new = GiveAffinity(EdgeFilePath="datasets/{}/{}".format(dataset, dict_files[list_files[i+1]]), g=g, epsilon=epsilon)
			print("Afinity Matrices computed, about to find Similarity")
			sim_score = Similarity(AM_old, deepcopy(AM_new))
			f.write(str(sim_score))
			f.write("\n")
			print("Time taken for computing sim score between {} and {} is {} secs".format(dict_files[list_files[i]], dict_files[list_files[i+1]], (time.time()-start)))
	print("The scores have been documented")
	return None 

def find_anomalies(results_dir, dataset, param[0], param[1]):
	path = results_dir+dataset+"/"+"time_series"+"_"+str(g)+"_"+str(round(epsilon,2))+".txt"
	time_series = np.loadtxt(path)
	mean_, median_, lower_t, upper_t = give_stats(time_series)
	anomalous_similarities = []
	with open(results_dir+dataset+"/"+"anomalous_similarities"+"_"+str(g)+"_"+str(round(epsilon,2))+".txt", "w+") as f:
		for i in range(0, time_series.shape[0]):
			if time_series[i] < lower_t:
				anomalous_similarities.append(i)
				f.write(str(anomalous_similarities))
				f.write("\n")
	with open(results_dir+dataset+"/"+"anomalous_time_stamp"+"_"+str(g)+"_"+str(round(epsilon,2))+".txt", "w+") as f:
		for i in range(1, len(anomalous_similarities)):
			if anomalous_similarities[i]-anomalous_similarities[i-1] == 1:
				f.write(str(anomalous_similarities[i]))
				f.write("\n")
	print("Anomalies written to the results folder ")
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
		find_anomalies(results_dir, dataset, param[0], param[1])

	
