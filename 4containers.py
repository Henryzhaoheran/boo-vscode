# P43 the other 4 containers

# deque add data on the left.
from collections import deque

queue1 = ['hello', 'my', 'friend']

queue2 =deque(['unbeatable', 'means', 'lonely'])
print(type(queue1))
print(type(queue2))



queue1.append('msg')
print(queue1)

#queue1.appendleft()
queue11 = deque(queue1)
queue11.appendleft('Hello')

print(type(queue11))
print("queue3 is %", queue11)


queue2.appendleft('head')
print(queue2)

for w in queue2:
    print(w)