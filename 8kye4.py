def find_it(seq):
	hash_list = ()
	for i in seq:
		if i not in hash_list and seq.count(i) % 2 > 0:
			return i
		else:
			hash_list += (i,)


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))