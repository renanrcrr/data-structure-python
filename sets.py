c1 = {1, 2, 3}
c2 = {'danielle', 'leal', 'sampaio'}
c3 = {1, 'danielle', 3.14}
c4 = set([1,2,2,3,3])

print(len(c2))
if 'danielle' in c2:
	print('found')

c5 = {1, 2, 3, 4}
c6 = {3, 4, 5, 6}

print(c5 | c6) 
print(c5 & c6) 
print(c6 - c5) 

c = {10, 20, 30, 40}
c.remove(20)

print(c)