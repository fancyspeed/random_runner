
p_learn = ('../raw_data/log_learn.csv', '../data/linenum_learn', '../raw_data/enrollment_learn.csv')
p_valid = ('../raw_data/log_valid.csv', '../data/linenum_valid', '../raw_data/enrollment_valid.csv')
p_train = ('../raw_data/log_train.csv', '../data/linenum_train', '../raw_data/enrollment_train.csv')
p_test = ('../raw_data/log_test.csv', '../data/linenum_test', '../raw_data/enrollment_test.csv')

import json
for pin, pout, peid in [p_learn, p_valid, p_train, p_test]:
  with open(pout, 'w') as fo:
    for line in open(peid):
        eid = line.split(',')[0]
        uid = line.split(',')[1]
        feats = {'line_num':int(eid)}
        fo.write('%s\t%s\n' % (eid, json.dumps(feats)))

