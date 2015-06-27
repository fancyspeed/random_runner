
p_learn = ('../raw_data/log_learn.csv', '../data/coursenum_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/coursenum_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/coursenum_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/coursenum_test', '../raw_data/enrollment_test.csv')

uid_num = {}
for line in open('../raw_data/enrollment_train.csv'):
    eid, uid, cid = line.strip().split(',')
    uid_num[uid] = uid_num.get(uid, 0) + 1
for line in open('../raw_data/enrollment_test.csv'):
    eid, uid, cid = line.strip().split(',')
    uid_num[uid] = uid_num.get(uid, 0) + 1

import json
for pin, pout, peid in [p_learn, p_valid, p_train, p_test]:
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        uid = line.split(',')[1]
        if uid in uid_num:
            feats = {'course_num':uid_num[uid]}
            fo.write('%s\t%s\n' % (eid, json.dumps(feats)))

