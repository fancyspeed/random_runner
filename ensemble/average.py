import sys
if len(sys.argv) < 3:
    print 'usage: out in...'

len_f = len(sys.argv) - 2
idx_f = 0
p_list = []
for f in sys.argv[2:]:
    idx_i = 0
    for line in open(f):
        if idx_f == 0:
            p_list.append([float(line.strip())])
        else:
            p_list[idx_i].append(float(line.strip()))
        idx_i += 1
    idx_f += 1

with open(sys.argv[1], 'w') as fo:
    for ps in p_list:
        p = sum(ps) / len(ps)
        fo.write('%s\n' % p)
