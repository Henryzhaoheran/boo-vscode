# List generator P42
# 列表生成式和列表生成器的不同

l = ("{}*{}".format(x, x) for x in range(1, 11))
print(l)
"""
print(next(l))
print(next(l))
print(next(l))
print(next(l))
"""

for idx in range(1, 11):
    print(next(l), end = ' ')
print()

#判断为偶数
l1 = ("_{}_".format(x) for x in range(1, 11) if x%2 == 0)
print(l1)
"""
print(next(l))
print(next(l))
print(next(l))
print(next(l))
"""

for idx in range(1, 6):
    print(next(l1), end = ' ')
print()


