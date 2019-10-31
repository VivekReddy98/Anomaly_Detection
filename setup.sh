#!/bin/bash

export GDMPATH=/home/vkarri/Anomaly_Detection
export SPARK_HOME=/usr/local/spark-2.4.4-bin-hadoop2.7/
echo $GDMPATH
export PYSPARK_PYTHON=$GDMPATH/venv/bin/python3 
echo $PYSPARK_PYTHON
export PYSPARK_DRIVER_PYTHON=$GDMPATH/venv/bin/python3
export PYTHONPATH=$PYTHONPATH:$GDMPATH/

