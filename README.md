## random_runner

## requiremens:
  * tools/xgboost3: https://github.com/dmlc/xgboost

## steps:
  
  * raw\_data: split\_to\_valid.py
  * prepare: get\_feat\_xxx.py; join\_feats\_nosampleing.py
  * boost: run\_xgboost2.sh
  * result: red\_test.csv
