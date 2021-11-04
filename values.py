import yaml
from collections.abc import MutableMapping
import pandas as pd

# d = {'a':1,'c':{'a':2,'b':{'x':5,'y':10}},'d':[1,2,3]}

# log path
log_path = '/Users/jason/Documents/test-deploy/values_log.txt'
f = open(log_path,'w',encoding='utf-8')

# read yaml file func
def read_yaml(file):
    with open(file,'r',encoding='utf8') as f:
        data = yaml.safe_load(f)
    return data

# import data
a = read_yaml('/Users/jason/Documents/sensestar/sw-infra/helm/sw-api/values-test.yaml')
# a = read_yaml('/Users/jason/Documents/test-deploy/123.yaml')

# flatten data func in dictonary
def flatten_dict(a: MutableMapping, sep: str= '_') -> MutableMapping:
    [flat_dict] = pd.json_normalize(a, sep=sep).to_dict(orient='records')
    return flat_dict

# print(flatten_dict(a),file=f)
print(type(flatten_dict(a)))