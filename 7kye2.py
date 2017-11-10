def tickets(people):
	money = {25:0, 50:0}
	print(people)
	for orders in people:
		if orders == 25: 
			money[25] += 1
		elif orders == 50:
			if money[25] == 0:
				return "NO"
			else:
				money[25] -= 1
				money[50] += 1
		elif orders == 100:
			if money[50] >= 1 and money[25] >= 1:
				money[50] -= 1
				money[25] -= 1
			elif money[25] > 3:
				money[25] -= 3
			else:
				return "NO"
	return "YES"


print(tickets([25, 25, 50]))