def friend(x):
	result_list = [value for value in x if len(value) == 4 ]
	return result_list



if __name__ == "__main__":
	print(friend(["Ryan", "Kieran", "Mark",]))