
p_learn = ('../raw_data/log_learn2.csv', '../data/interval_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid2.csv', '../data/interval_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train2.csv', '../data/interval_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test2.csv', '../data/interval_test', '../raw_data/enrollment_test.csv')

import time
def get_day(date):
    arr = date.split('T')[0].split('-')
    if len(arr) != 3: return 0
    t = time.mktime([int(arr[0]), int(arr[1]), int(arr[2])] + [0]*6)
    return int(t)/3600/24

import json
for pin, pout, peid in [p_learn, p_valid, p_train, p_test]:
  key_num = {}
  for line in open(pin):
    arr = line.strip().split(',')
    #1,9Uee7oEuuMmgPx2IzPfFkWgkHZyPbWr0,DPnLzkJJqOOPRJfBxIHbQEERiYHu5ila,2014-06-14T09:38:29,server,nagivate,Oj6eQgzrdqBMlaCtaq1IkY6zruSrb71b
    #3,1qXC7Fjbwp66GPQc6pHLfEuO8WKozxG4,7GRhBDsirIGkRZBtSMEzNTyDr2JQm4xx,2014-06-19T08:43:59,server,access,jU152iC3MSAYCcXrcBy5IohAGjqKttZn,sequential,2014-06-19T00:00:00
    eid = arr[0]
    if len(arr) == 9:
        if eid not in key_num: key_num[eid] = [] 
        day1, day2 = get_day(arr[3]), get_day(arr[-1])
        if day1 and day2:
            diff = day1-day2
            if diff >= 0:
                key_num[eid].append(diff)
  key_num2 = {}
  for eid in key_num:
    if not key_num[eid]: continue 
    key_num2[eid] = {}
    key = 'object_interval_last'
    key_num2[eid][key] = key_num[eid][-1] 
    avg = sum(key_num[eid]) / float(len(key_num[eid]))
    key = 'object_interval_avg'
    key_num2[eid][key] = avg 
    if len(key_num[eid]) >= 2:
        key = 'object_interval_last2avg'
        key_num2[eid][key] = key_num[eid][-1]/(avg + 0.01) 
  key_num = key_num2
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

