coins = [100, 50, 5, 1]
result = []
sum = 0
rest = 60 

i = 0

while i < len(coins) and sum != rest:

	if sum + coins[i] <= rest:
		result.append(coins[i])
		sum += coins[i]
	else:
		i += 1

print(result)