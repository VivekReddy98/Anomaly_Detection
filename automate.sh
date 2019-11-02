echo "Please enter your choice of dataset"
read dataset

export start=$SECONDS
python Execute.py $dataset >> logs/$dataset.log

elapsedtime=$(($SECONDS-$start))
echo It took $elapsedtime seconds to complete the dataset $dataset on the complete search space provided in the json file >> time_taken.txt