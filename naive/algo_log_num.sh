awk -F"," '{if(NF==3){print $1","1.0/a[$1]}else{a[$1]+=1}}' ../raw_data/log_valid.csv ../raw_data/enrollment_valid.csv > out.valid
python ../evaluate/metric_AUC.py ../raw_data/truth_valid.csv out.valid

#awk -F"," '{if(NF==3){print $1","1.0/a[$1]}else{a[$1]+=1}}' ../raw_data/log_test.csv ../raw_data/enrollment_test.csv > out.test
