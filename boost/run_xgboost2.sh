
BIN=../../tools/xgboost3/xgboost

round=120
depth=5
model=0120.model

$BIN xgboost2.conf num_round=$round bst:max_depth=$depth data=../data/learn eval[test]=../data/learn
$BIN xgboost2.conf task=pred model_in=$model test:data=../data/valid
$BIN xgboost2.conf task=dump model_in=$model

python ../evaluate/construct_pred.py ../data/pred_valid.csv ../raw_data/truth_valid.csv ../boost/pred.txt 
python ../evaluate/metric_AUC.py ../raw_data/truth_valid.csv ../data/pred_valid.csv
mv pred.txt pred_valid.txt

$BIN xgboost2.conf num_round=$round bst:max_depth=$depth data=../data/train eval[test]=../data/train
$BIN xgboost2.conf task=pred model_in=$model test:data=../data/test
python ../evaluate/construct_pred.py ../data/pred_test.csv ../raw_data/truth_test.csv ../boost/pred.txt 
mv pred.txt pred_test.txt
