import sys

def needleman_wunsch(s1, s2, match, mismatch, gap):	
	cols, lin = len(s1) + 1, len(s2) + 1

	mat = [[0 for i in range(cols)] for i in range(lin)]

	traceback = {}

	mat[0][0] = 0
	
	for i in range(1, cols):
		mat[0][i] = mat[0][i - 1] + gap
	
		traceback[(0, i)] = (0, i - 1)
	
	for i in range(1, lin):
		mat[i][0] = mat[i - 1][0] + gap
		
		traceback[(i, 0)] = (i - 1, 0)

	def max_valor(i, j):
		v1 = mat[i - 1][j - 1] + (match if s2[i - 1] == s1[j - 1] else mismatch) 
		
		v2 = mat[i - 1][j] + gap 
		
		v3 = mat[i][j - 1] + gap 

		max_v = max([v1, v2, v3])

		if max_v == v1:
			traceback[(i, j)] = (i - 1, j - 1)
		
		elif max_v == v2:
			traceback[(i, j)] = (i - 1, j)
		
		else:
			traceback[(i, j)] = (i, j - 1)

		return max_v

	for i in range(1, lin):
		for j in range(1, cols):
			mat[i][j] = max_valor(i, j)

	s1_result, s2_result = '', '' 
	
	i, j = lin - 1, cols - 1 

	while True:
		i_next, j_next = traceback[(i, j)]

		if (i - 1) == i_next and (j - 1) == j_next: 
			s1_result += s1[j_next]
			
			s2_result += s2[i_next]
			
		elif (i - 1) == i_next and j == j_next: 
			s1_result += '-'
			
			s2_result += s2[i_next]
			
		elif i == i_next and (j - 1) == j_next: 
			s1_result += s1[j_next]
			
			s2_result += '-'

		i, j = i_next, j_next

		if not i and not j:
			break

	s1_result, s2_result = s1_result[::-1], s2_result[::-1]

	print('{0}\n{1}'.format(s1_result, s2_result))



if __name__ == "__main__":
	len_args = len(sys.argv)

	if len_args == 6:
		s1, s2 = sys.argv[1], sys.argv[2]
		
		match, mismatch, gap = sys.argv[3], sys.argv[4], sys.argv[5]
		
		needleman_wunsch(s1, s2, int(match), int(mismatch), int(gap))

	else:
		print('\nExecute:\n\tpython needleman_wunsch.py <sequence1> <sequence2> <match> <mismatch> <gap>')
		
		print('\nExample:\n\tpython needleman_wunsch.py GCATGCU GATTACA 1 -1 -1\n')
