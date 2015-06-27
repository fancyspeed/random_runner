
rate = 3

for f1, f2 in [('truth_learn2.csv', 'truth_learn.csv'),
               ('truth_train2.csv', 'truth_train.csv'),
               ]:
  with open(f1, 'w') as fo:
    trains = []
    for line in open(f2):
        label = line.strip().split(',')[1]
        if label == '0':
            for i in range(rate):
                trains.append(line)
        else:
            trains.append(line)
    import random
    random.shuffle(trains)
    for line in trains:
        fo.write(line)
