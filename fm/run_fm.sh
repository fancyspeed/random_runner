BIN=../../tools/libfm/bin/libFM

# MCMC
$BIN -task c -train ../data/learn -validation ../data/learn -test ../data/valid -out pred.txt -dim '1,1,8' -method mcmc -iter 100 -init_stdev 0 -verbosity 1
# SGDA 
#$BIN -task r -train $TRAIN -validation $VALID -test $TEST -out $PRED -dim '1,1,0' -method sgda -iter 100 -learn_rate 0.01 -init_stdev 0 -verbosity 1
# ALS 
#$BIN -task r -train $TRAIN -validation $VALID -test $TEST -out $PRED -dim '1,1,0' -method als -iter 100 -regular '0,0,1' -init_stdev 0 -verbosity 1
# SGD
#$BIN -task r -train $TRAIN -validation $VALID -test $TEST -out $PRED -dim '1,1,0' -method sgd -iter 100 -learn_rate 0.01 -regular '0,0,1' -init_stdev 0 -verbosity 1

python ../evaluate/construct_pred.py ../data/pred_valid.csv ../raw_data/truth_valid.csv ../fm/pred.txt 
python ../evaluate/metric_AUC.py ../raw_data/truth_valid.csv ../data/pred_valid.csv
mv pred.txt pred_valid.txt
