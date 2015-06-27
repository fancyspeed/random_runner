awk -F"," '{if(NF==2)a[$1]=$2;else{ b[$3]+=1;c[$3]+=a[$1];}}END{for(v in b)print v","(c[v]+0.0)/b[v]}' truth_train.csv enrollment_train.csv > m
awk -F"," '{if(NF==2)a[$1]=$2;else{ print $1","a[$3];}}END{}' m enrollment_test.csv > t
