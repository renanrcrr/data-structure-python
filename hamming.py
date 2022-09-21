def hamming(s1, s2):
	len_s1, len_s2 = len(s1), len(s2)

	if len_s1 != len_s2:
		raise ValueError('Different size strings!')

	return sum(1 for i in range(len_s1) if s1[i] != s2[i])

print(hamming('renan', 'rodrigues'))
print(hamming('0001', '1100'))
print(hamming('python', 'pytohn'))