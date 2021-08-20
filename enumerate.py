## enumerate P41

# example 1
ex_list = ['Mon', 'Tue', 'Wed']

for idx in range(0, len(ex_list)):
    print(idx, ex_list[idx])

# example 2
ex2_list = ['yellow', 'blue', 'red']
i = 0

for element in ex2_list:
    print(i, ex2_list[i])
    i = i + 1


# enumerate example 3
my_list = ['Bob', 'George', 'Henry']
for a, b in enumerate(my_list):
    print(a,b)



# enumerate example 4
for i, j in enumerate('abc'):
    print(i, j)
    print(j, i)


# 列表生成式 List Comprehensions
em_list = []
for x in range(1, 11):
    em_list.append("{}x{}".format(x, x))
print(em_list)


# [value  Loop]
l1 = ["{}+{}".format(x, x) for x in range(10, 21)]
print(l1)


# 右边加入判断 if x%5 == 0
l2 = [x for x in range(0, 101) if x%5 == 0 ]
print(l2)


# 左右边加入判断
l3 = [x if x>5 else 0 for x in range(0, 101) if x%5 == 0 ]
print(l3)
