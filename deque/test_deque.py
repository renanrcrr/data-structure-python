from collections import deque

d = deque()

d.append(1) # add from the right side
d.appendleft(2) 
d.append(3)
d.appendleft(4)
print(d)
d.remove(3) # remove the element
d.popleft()
d.pop() # remove from the right side

for i in d:
	print(i, end=' ')