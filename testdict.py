# test Id
import copy
a = ['a', [1,2]] #list in list
b = a.copy
print(id(a))
print(id(b))
print(a)
print(b)

c = a
d = copy.deepcopy(a)
print(id(d[1]))
print(id(a[1]))




'''
# Test list append
user_list = []
user_list.append("hello")
print(user_list)
'''


'''
# Test dict
testdict = dict()
testdict = {'name1':'bob', 'name2':'jack', 'name3':'tom'}
testdict['name4']='Will'
testdict['name1']='Briget'
print(testdict)

print(type(testdict))
'''

