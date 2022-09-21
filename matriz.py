matriz = [
	['Bruno', 8, 7, 6],
	['Igo', 4.5, 9, 10],
	['Diego', 6, 6, 8],
]

for linha in matriz:
	for col in linha:
		print(str(col) + '\t', end = ' ')
		
	print('')