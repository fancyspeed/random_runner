
p_learn = ('../raw_data/log_learn.csv', '../data/userid_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/userid_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/userid_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/userid_test', '../raw_data/enrollment_test.csv')

import time
def get_day(date):
    arr = date.split('T')[0].split('-')
    if len(arr) != 3: return 0
    t = time.mktime([int(arr[0]), int(arr[1]), int(arr[2])] + [0]*6)
    return int(t)/3600/24

import json
for pin, pout, peid in [p_learn, p_valid, p_train, p_test]:
  key_num = {}
  cur_key = []
  for line in open(pin):
    arr = line.strip().split(',')
    #1,9Uee7oEuuMmgPx2IzPfFkWgkHZyPbWr0,DPnLzkJJqOOPRJfBxIHbQEERiYHu5ila,2014-06-14T09:38:29,server,nagivate,Oj6eQgzrdqBMlaCtaq1IkY6zruSrb71b
    eid = arr[0]
    day = int(arr[3].split('T')[0].replace('-', ''))
    if not cur_key or eid == cur_key[0][0]:
        if eid not in key_num: key_num[eid] = {}
        #key = 'user_id_%s' % arr[1]
        #key_num[eid][key] = 1
        cur_key.append((eid, day, arr[5], arr[6]))
    else:
        eid = cur_key[0][0] 
        key = 'lasttime_cate_%s' % cur_key[-1][2]
        key_num[eid][key] = 1 
        key = 'lasttime_object_%s' % cur_key[-1][3]
        key_num[eid][key] = 1 
        cur_key = []
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

