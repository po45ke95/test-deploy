def read(file):
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
    return data
# v = read('/Users/jason/Documents/sensestar/sw-infra/helm/sw-api/values-test.yaml') # this row is on mac env.
v = read('C:\\Users\\Peter\\Documents\\Company\\sensestar\\sw-infra\\helm\\sw-api\\values-test.yaml') # this row is windows env.
t1 = []

# clane values row data
for x in v:
    t1.append(x.replace('\n', '').replace('-', '').replace(',', '') )

# get list len
listcount = len(t1)

# write file
# path = '/Users/jason/Documents/test-deploy/value-logs.txt' # this row is on mac env.
path = 'C:\\Users\\Peter\\Documents\\Company\\test-deploy\\value-logs.txt' # this row is windows env.
f = open(path,'w',encoding='utf-8')

for i in range(listcount):
    try:
        if len(t1[i])>0:
            print((t1[i]),file=f)
        else:
            pass
    except IndexError:
        continue

f.close()