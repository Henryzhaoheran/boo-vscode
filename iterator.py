# P42 9:00
# 

from collections import Iterable
from collections import Iterator
# Iterable 迭代器对象 Iterator 迭代器
# 迭代器对象的作用就是判断它是否可迭代的。


message = "there is a beautiful jungle"

for word in message:
    print(word, end="_")
print()
