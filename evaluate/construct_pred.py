import sys
if len(sys.argv) != 4:
  print '<usage> out in pred'
  exit(1)
with open(sys.argv[1], 'w') as fo:
    with open(sys.argv[2]) as fin:
        for line in open(sys.argv[3]):
            pred = line.strip()
            eid = fin.readline().strip().split(',')[0]
            fo.write('%s,%s\n' % (eid, pred))
