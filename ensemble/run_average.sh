python average.py pred.txt ../boost/pred_valid.txt ../fm/pred_valid.txt
python ../evaluate/construct_pred.py ../data/pred_valid.csv ../raw_data/truth_valid.csv ../ensemble/pred.txt 
python ../evaluate/metric_AUC.py ../raw_data/truth_valid.csv ../data/pred_valid.csv
