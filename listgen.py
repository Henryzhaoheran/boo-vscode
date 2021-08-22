# List generator P42
# 列表生成式和列表生成器的不同

l = ("{}*{}".format(x, x) for x in range(1, 11))
print(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))