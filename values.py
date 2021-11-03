import collections

def read(file):
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
    return data
z = read('/Users/jason/Documents/sensestar/sw-infra/helm/sw-api/values-test.yaml') # this row is on mac env.
# v = read('C:\\Users\\Peter\\Documents\\Company\\sensestar\\sw-infra\\helm\\sw-api\\values-test.yaml') # this row is windows env.
# t1 = []

# clane values row data
# for x in v:
#     t1.append(x.replace('\n', '').replace('-', '').replace(',', '').split(':'))

def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
print(dict(z))
# get list len
# listcount = len(t1)

# write file
# path = '/Users/jason/Documents/test-deploy/value-logs.txt' # this row is on mac env.
# path = 'C:\\Users\\Peter\\Documents\\Company\\test-deploy\\value-logs.txt' # this row is windows env.
# f = open(path,'w',encoding='utf-8')

# for i in range(listcount):
#     try:
#         if len(t1[i])>0:
#             print((t1[i]),file=f)
#         else:
#             pass
#     except IndexError:
#         continue

# f.close()