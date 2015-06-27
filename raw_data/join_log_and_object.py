
key_dict = {}
for line in open('object.csv'):
    arr = line.strip().split(',')
    key = arr[0]+','+arr[1]
    key_dict[key] = [arr[2], arr[4]]

for pin, pout in [
                  ('log_learn.csv', 'log_learn2.csv'),
                  ('log_valid.csv', 'log_valid2.csv'),
                  ('log_train.csv', 'log_train2.csv'),
                  ('log_test.csv', 'log_test2.csv'),
                  ]:
    with open(pout, 'w') as fo:
        for line in open(pin):
            arr = line.strip().split(',')
            #1,9Uee7oEuuMmgPx2IzPfFkWgkHZyPbWr0,DPnLzkJJqOOPRJfBxIHbQEERiYHu5ila,2014-06-14T09:38:29,server,nagivate,Oj6eQgzrdqBMlaCtaq1IkY6zruSrb71b
            key = arr[2]+','+arr[-1]
            if key in key_dict:
                arr += key_dict[key] 
            fo.write(','.join(arr) + '\n')
