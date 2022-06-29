def power(N, P):


	if P == 0: # base condition
		return 1

	
	return (N*power(N, P-1))


N = 5
P = 0

print(power(N, P))
