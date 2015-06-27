
p_learn = ('../raw_data/log_learn.csv', '../data/lastdaynum_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/lastdaynum_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/lastdaynum_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/lastdaynum_test', '../raw_data/enrollment_test.csv')

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
        cur_key.append((eid, day))
    else:
        eid = cur_key[0][0]
        key = 'lastday_lognum'
        for pair in cur_key:
            if pair[1] == cur_key[-1][1]:
                key_num[eid][key] = key_num[eid].get(key, 0) + 1
        cur_key = []
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        if eid in key_num:
            fo.write('%s\t%s\n' % (eid, json.dumps(key_num[eid])))

