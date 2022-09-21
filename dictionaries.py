d = {} 

d['joao'] = 21
d['maria'] = 20
d['pedro'] = 35

for k in d.keys():
	print(d[k])

chave_procurada = 'joao'

if chave_procurada in d.keys():
	print('key found')
else:
	print('key did not find')

del d['joao']