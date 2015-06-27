
learns = (('../data/lognum_learn','../data/lastdaynum_learn','../data/interval_learn',
           '../data/coursenum_learn','../data/lastdaywait_learn','../data/variance_learn',
           '../data/dayseq_learn', '../data/daycate_learn', '../data/courseid_learn',
           '../data/linenum_learn',
          ), 
          '../raw_data/truth_learn.csv', '../data/learn')
valids = (('../data/lognum_valid','../data/lastdaynum_valid','../data/interval_valid',
           '../data/coursenum_valid','../data/lastdaywait_valid','../data/variance_valid',
           '../data/dayseq_valid', '../data/daycate_valid', '../data/courseid_valid',
           '../data/linenum_valid',
          ), 
          '../raw_data/truth_valid.csv', '../data/valid')
trains = (('../data/lognum_train','../data/lastdaynum_train','../data/interval_train',
           '../data/coursenum_train','../data/lastdaywait_train','../data/variance_train',
           '../data/dayseq_train', '../data/daycate_train', '../data/courseid_train',
           '../data/linenum_train',
          ), 
          '../raw_data/truth_train.csv', '../data/train')
tests =  (('../data/lognum_test','../data/lastdaynum_test','../data/interval_test',
           '../data/coursenum_test','../data/lastdaywait_test','../data/variance_test',
           '../data/dayseq_test', '../data/daycate_test', '../data/courseid_test',
           '../data/linenum_test',
          ), 
          '../raw_data/truth_test.csv', '../data/test')

import json
feat_dict = {}

eid_feats = {}
with open(learns[2], 'w') as fo:
    for f in learns[0]:
        for line in open(f):
            eid, feats = line.strip().split('\t')
            if eid not in eid_feats:
                eid_feats[eid] = {}
            feats = json.loads(feats)
            for feat in feats:
                if feat not in feat_dict:
                    feat_dict[feat] = len(feat_dict) + 1
                eid_feats[eid][feat_dict[feat]] = feats[feat]
    for line in open(learns[1]):
        eid, label = line.strip().split(',')
        flist = ['%s:%s' % (k, v) for k, v in sorted(eid_feats[eid].items(), key=lambda d:d[0])]
        fo.write('%s %s\n' % (label, ' '.join(flist)))

eid_feats = {}
with open(valids[2], 'w') as fo:
    for f in valids[0]:
        for line in open(f):
            eid, feats = line.strip().split('\t')
            if eid not in eid_feats:
                eid_feats[eid] = {}
            feats = json.loads(feats)
            for feat in feats:
                if feat not in feat_dict:
                    continue
                eid_feats[eid][feat_dict[feat]] = feats[feat]
    for line in open(valids[1]):
        eid, label = line.strip().split(',')
        flist = ['%s:%s' % (k, v) for k, v in sorted(eid_feats[eid].items(), key=lambda d:d[0])]
        fo.write('%s %s\n' % (label, ' '.join(flist)))

eid_feats = {}
with open(trains[2], 'w') as fo:
    for f in trains[0]:
        for line in open(f):
            eid, feats = line.strip().split('\t')
            if eid not in eid_feats:
                eid_feats[eid] = {}
            feats = json.loads(feats)
            for feat in feats:
                if feat not in feat_dict:
                    continue
                eid_feats[eid][feat_dict[feat]] = feats[feat]
    for line in open(trains[1]):
        eid, label = line.strip().split(',')
        flist = ['%s:%s' % (k, v) for k, v in sorted(eid_feats[eid].items(), key=lambda d:d[0])]
        fo.write('%s %s\n' % (label, ' '.join(flist)))

eid_feats = {}
with open(tests[2], 'w') as fo:
    for f in tests[0]:
        for line in open(f):
            eid, feats = line.strip().split('\t')
            if eid not in eid_feats:
                eid_feats[eid] = {}
            feats = json.loads(feats)
            for feat in feats:
                if feat not in feat_dict:
                    continue
                eid_feats[eid][feat_dict[feat]] = feats[feat]
    for line in open(tests[1]):
        eid, label = line.strip().split(',')
        flist = ['%s:%s' % (k, v) for k, v in sorted(eid_feats[eid].items(), key=lambda d:d[0])]
        fo.write('%s %s\n' % (label, ' '.join(flist)))

