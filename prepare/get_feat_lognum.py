
p_learn = ('../raw_data/log_learn.csv', '../data/lognum_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/lognum_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/lognum_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/lognum_test', '../raw_data/enrollment_test.csv')

import json
import math
for pin, pout, peid in [p_learn, p_valid, p_train, p_test]:
  key_num = {}
  for line in open(pin):
    arr = line.strip().split(',')
    #1,9Uee7oEuuMmgPx2IzPfFkWgkHZyPbWr0,DPnLzkJJqOOPRJfBxIHbQEERiYHu5ila,2014-06-14T09:38:29,server,nagivate,Oj6eQgzrdqBMlaCtaq1IkY6zruSrb71b
    eid = arr[0]
    if eid not in key_num: key_num[eid] = {}
    key = 'total_lognum'
    key_num[eid][key] = key_num[eid].get(key, 0) + 1
    key = arr[4]+'_'+arr[5]
    key_num[eid][key] = key_num[eid].get(key, 0) + 1
  for eid in key_num:
    num = key_num[eid]['total_lognum']
    v = min(12, int(math.log(num+1, 2)))
    key = 'total_lognum_%s' % v
    key_num[eid][key] = 1
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

