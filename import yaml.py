import yaml
dict1 = {1:'a', 2:'b',3:'c',4:'d'}
list1 = [1,2,3,4]
tup1 = ('x','b','c')

print(yaml.dump(dict1,default_flow_style=False))
print(yaml.dump(list1,default_flow_style=False))
print(yaml.dump(tup1,default_flow_style=False))
