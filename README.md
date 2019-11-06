# Anomaly Detection in Time Varying Graphs
A course project completed to satisfy the requirements of CSC 591 Graph Data Mining at NC State University.

## Project Setup Guide:

### Clone and Create a Virtual Environment.
0) Clone this repositiry preferabbly in /home/unityID/ dir
1) Install virtual environment package:
2) sudo apt-get install python-virtualenv
3) Create a virtual environment inside your project directory using 
4) virtualenv -p /usr/bin/python3 project_directory/venv (The second argument is the name of the folder which will be created, you might not want to change it)
5) cd Anomaly_Detection
6) source venv/bin/activate (to start the virtual environment)
6) pip install -r requirements.txt (To install required packages)

### Execute your set_up.sh to set the required environemt variables.
Note: Edit the set_up.sh to match the paths on your machine. (nano set_up.sh)
1) source set_up.sh

### Copy datasets folder into the project directory

### Source Code Walkthrough
1) DeltaCon and GenerateGraphMatrices are two important classes implemented and packaged under the utils directory.
2) Similarity, Moving Average and other trivial functions have been implemneted in anomaly.py script

### Steps to execute the code.
1) Use python anomaly.py "dataset_name"
2) To edit the hyperparams open the search_hyper_param.json and edit the params of the dataset you want to.
3) Similarity Scores will be writen to results/dataset/* folder under the name time_series_g_epsilon.txt.
4) Anomalous Similarities and Anomalous Timestamps are also stored in the same folder.
5) As per the requirements time series data in also outputted by the name "dataset_time_series.txt" in the project root directory.
6) The Plots of Similarity Scores vs Time-Stamp has been documented in P4_report
