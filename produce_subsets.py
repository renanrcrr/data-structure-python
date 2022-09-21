def produce_subsets(S, vet, K, N):
	if K == N:
		print('{', end=' ')
		
		for i in range(N):
			if vet[i] == True:
				print('%d' % S[i], end=' ')
		
		print('}')
	
	else:
		vet[K] = True
		
		produce_subsets(S, vet, K + 1, N)
		
		vet[K] = False
		
		produce_subsets(S, vet, K + 1, N)

S = [1, 2, 3]

tamS = len(S)

vet = [False for i in range(tamS)]

produce_subsets(S, vet, 0, tamS)