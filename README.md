# Anomaly Detection
A course project for CSC 591 Graph Data Mining at NC State University.

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

### Download Apache Spark 2.4.4.
1) Java 8, Scala and Python 3 are assumed to be installed, they are in VCL ADBI image.
2) Download Spark 2.4.4 and extract using these commands.
3) wget http://mirrors.koehn.com/apache/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
4) tar xvf spark-x.x.x-bin-hadoopx.x.xxx
5) mv spark-x.x.x-bin-hadoopx.x.xxx /usr/local/

### Download graphframes jar in your project directory
1) wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar

### Execute your set_up.sh to set the required environemt variables.
Note: Edit the set_up.sh to match the paths on your machine.
1) source set_up.sh

### Copy datasets folder into the project directory

## Command to execute:
1) $SPARK_HOME/bin/spark-submit graphframes-x.x.x-sparkx.x-s_x.x.jar *.py arg0 arg1 arg2 .... 
