def read(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data
v = read('/Users/jason/Documents/sensestar/sw-infra/helm/sw-api/templates/client-api/deployment.yaml')
t1 = []

# clean row data
for x in v:
    t1.append((x.replace('\n', '')).replace('.Values.', '').replace('- if', '').replace(' | trunc 15', '')
    .replace('30', '').replace('5', '').replace('1', '').replace('0644', '')
    .replace('apps/v', '').replace('Deployment', '').replace('namespace', '').replace('default', '')
    .replace('- end', '').replace('-config', '').replace(' toYaml ', '').replace(' include ' , '')
    .replace(' | indent 4 ', '').replace(' | indent 6 ', '').replace(' | indent 8 ', '').replace(' | indent 10 ', '')
    .replace('{{- else }}', '').replace('config.yaml', '')
    .replace(' include "labels.standard" $ ', '').replace(' | quote ', '')
    .replace(' eq ', '').replace('$', '').replace('"', '')
    .replace('-', '').replace("{{-", "").replace("{{", "").replace("}}", "")
    .replace(' ','').replace('  ', '').replace('    ', '').replace('      ', '').split(':'))

# get list len for take data
listcount = len(t1)

# write file to check
path = '/Users/jason/Documents/test-deploy/clientapi-logs.txt'
f = open(path, 'w')

#for loop take list [1] data 
for i in range(listcount):
    try:
        if len(t1[i][1])>0:
            print((t1[i][1]),file=f)
        else:
            pass
    except IndexError:
        continue

f.close()