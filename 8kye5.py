#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...

def row_sum_odd_numbers(n):
	first_symbol = 1
	for i in range(n - 1):
		for j in range(n - i - 1):
			first_symbol += 2

	return sum([first_symbol + x * 2 for x in range(n)])
	
print(row_sum_odd_numbers(3))