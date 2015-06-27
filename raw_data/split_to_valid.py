import random

train_rate = 0.7

learn, valid = set(), set()
with open('truth_learn.csv', 'w') as fo1:
    with open('truth_valid.csv', 'w') as fo2:
        for line in open('truth_train.csv'):
            if random.random() <= 0.7:
                fo1.write(line) 
                learn.add(line.split(',')[0])
            else:
                fo2.write(line)
                valid.add(line.split(',')[0])

with open('enrollment_learn.csv', 'w') as fo1:
    with open('enrollment_valid.csv', 'w') as fo2:
        for line in open('enrollment_train.csv'):
            eid = line.split(',')[0]
            if eid in learn:
                fo1.write(line)
            elif eid in valid:
                fo2.write(line)

with open('log_learn.csv', 'w') as fo1:
    with open('log_valid.csv', 'w') as fo2:
        for line in open('log_train.csv'):
            eid = line.split(',')[0]
            if eid in learn:
                fo1.write(line)
            elif eid in valid:
                fo2.write(line)
