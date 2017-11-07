def high_and_low(numbers):
	numbers = [int(x) for x in numbers.split(' ')]
	numbers = "%s %s" %(str(max(numbers)), str(min(numbers)))
	return numbers

if __name__ == "__main__":
	exmpl1 = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
	print(high_and_low(exmpl1))