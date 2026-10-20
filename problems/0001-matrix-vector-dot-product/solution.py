def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	# (1*1) + (2*2) row 1 * row 1 
	# row 2 * row 1 

	a_rows = len(a)
	a_cols = len(a[0])
	
	output = []
	
	b_len = len(b)

	if a_cols != b_len:
		return -1 

	else: 
		for i in range(a_rows):
			row_sum = 0
			for j in range(a_cols):
				row_sum += a[i][j]* b[j]
			
			output.append(row_sum)


	return output