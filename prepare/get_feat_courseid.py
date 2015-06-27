
p_learn = ('../raw_data/log_learn2.csv', '../data/courseid_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid2.csv', '../data/courseid_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train2.csv', '../data/courseid_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test2.csv', '../data/courseid_test', '../raw_data/enrollment_test.csv')

import time
def get_day(date):
    arr = date.split('T')[0].split('-')
    if len(arr) != 3: return 0
    t = time.mktime([int(arr[0]), int(arr[1]), int(arr[2])] + [0]*6)
    return int(t)/3600/24

import json
import math
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
        key = 'course_id_%s' % arr[2]
        key_num[eid][key] = 1

        if len(arr) == 9:
            day1, day2 = get_day(arr[3]), get_day(arr[-1])
            cur_key.append((eid, day, arr[5], day1-day2))
        else:
            cur_key.append((eid, day, arr[5]))

    else:
        eid = cur_key[0][0] 
        key = 'lastday_catenum'
        cates = set()
        for pair in cur_key:
            if pair[1] == cur_key[-1][1]:
                cates.add(pair[2])
        key_num[eid][key] = len(cates)
        for cate in cates:
            key = 'lastday_cate_%s' % cate
            key_num[eid][key] = 1
        waits = []
        for pair in cur_key:
            if pair[1] == cur_key[0][1] and len(pair) == 4:
                if pair[3] >= 0:
                    waits.append(pair[3])
        if waits:
            v = sum(waits)/float(len(waits))
            key = 'firstday_wait'
            key_num[eid][key] = v
            key = 'firstday_wait_log'
            key_num[eid][key] = min(13, math.log(v+1, 2)) 
        else:
            key = 'firstday_nowait'
            key_num[eid][key] = 1 
        cur_key = []
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

