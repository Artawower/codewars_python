# my practices
def tower_builder(n_floors):
	print(n_floors)
	space_count = 0
	tree = []
	if n_floors > 1:
		star_count = n_floors * 2 - 1
	else:
		return ['*']
	print(star_count)
	for i in range(n_floors):
		tree.insert(0, ' ' * space_count + 
					('*' * star_count)[space_count:star_count - space_count] + 
					' ' * space_count)
		space_count += 1
	

	return tree

# best practices
# def tower_builder(n):
    # return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]


for i in tower_builder(4):
	print(i)