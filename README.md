# Anomaly Detection in Time Varying Graphs
A course project completed to satisfy the requirements of CSC 591 Graph Data Mining at NC State University.

## Project Setup Guide:

### Clone and Create a Virtual Environment.
0) Clone this repositiry preferabbly in /home/unityID/ dir
1) Install virtual environment package:
2) sudo apt-get install python-virtualenv
3) Create a virtual environment inside your project directory using 
4) virtualenv -p /usr/bin/python3 project_directory/venv (The second argument is the name of the folder which will be created, you might not want to change it)
5) cd anomaly-detection
6) source venv/bin/activate (to start the virtual environment)
6) pip install -r requirements.txt (To install required packages)

### Execute your set_up.sh to set the required environemt variables.
Note: Edit the set_up.sh to match the paths on your machine.
1) source set_up.sh

### Copy datasets folder into the project directory

### Steps to execute the code.
1) Use python anomaly.py "dataset_name"
2) To edit the hyperparams open the search_hyper_param.json and edit the params of the dataset you want to.
3) Results will be writen to results/dataset/* folder under the name time_series_g_epsilon.txt.
