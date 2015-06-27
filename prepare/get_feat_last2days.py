
p_learn = ('../raw_data/log_learn.csv', '../data/lastdaywait_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/lastdaywait_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/lastdaywait_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/lastdaywait_test', '../raw_data/enrollment_test.csv')

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
    day = get_day(arr[3])
    if not cur_key:
        if eid not in key_num: key_num[eid] = {}
        cur_key.append((eid, day))
    elif eid == cur_key[0][0]:
        if day != cur_key[-1][1]:
            cur_key.append((eid, day))
    else:
        eid = cur_key[0][0]
        key = 'lastday_wait'
        if len(cur_key) >= 2:
            waitday = cur_key[-1][1] - cur_key[-2][1]
            key_num[eid][key] = waitday 
        cur_key = []
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

