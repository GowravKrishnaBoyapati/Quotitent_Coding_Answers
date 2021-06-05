def segment(x,space):
	n=len(spac)
	min,max=[0]*(n-x+1),-2**31-1
	for i in range(n-x):
		min[i]=2**31-1
		for j in range(i,i+x):
			if min[i] > space[j]:
				min[i]=space[j]
		if max < min[i]:
			max=min[i]
	return max
