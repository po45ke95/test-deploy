def read(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data
v = read('/Users/jason/Documents/sensestar/sw-infra/helm/sw-api/values-test.yaml')
t1 = []

# clane values row data
for x in v:
    t1.append(x.replace('\n', '').replace('-', '').replace(',', '') )

# get list len
listcount = len(t1)

# write file
path = '/Users/jason/Documents/test-deploy/value-logs.txt'
f = open(path, 'w')

for i in range(listcount):
    try:
        if len(t1[i])>0:
            print((t1[i]),file=f)
        else:
            pass
    except IndexError:
        continue

f.close()