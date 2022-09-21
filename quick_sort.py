def split(v, start, end):
	pivot = start

	for i in range(start + 1, end + 1):
		if v[i] <= v[start]:
			pivot += 1
			v[i], v[pivot] = v[pivot], v[i]

	v[pivot], v[start] = v[start], v[pivot]

	return pivot

def quick_sort(v, start, end):
	if end > start:
		pivot = split(v, start, end)

		quick_sort(v, start, pivot - 1)
		
		quick_sort(v, pivot + 1, end)

v = [50, 20, 70, 15]

quick_sort(v, 0, len(v) - 1)

print(v)