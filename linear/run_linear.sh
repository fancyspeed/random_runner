TRAIN_BIN=../../tools/liblinear/train
TEST_BIN=../../tools/liblinear/predict

#$TRAIN_BIN -s 7 -c 1 -e 0.01 ../data/learn dog.model
$TEST_BIN -b 1 ../data/valid dog.model pred.txt 
awk '{if(NR==1){if($2==1)idx=2;else idx=3;}else print $idx}' pred.txt > pred2.txt
mv pred2.txt  pred.txt
python ../evaluate/construct_pred.py ../data/pred_valid.csv ../raw_data/truth_valid.csv ../linear/pred.txt 
python ../evaluate/metric_AUC.py ../raw_data/truth_valid.csv ../data/pred_valid.csv
mv pred.txt pred_valid.txt
