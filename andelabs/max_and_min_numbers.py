def find_max_min(numbers):
	if min(numbers) == max(numbers):
		return [len(numbers)]
	else:
		return [min(numbers),max(numbers)]

print find_max_min([1, 2, 3, 4])
print find_max_min([6, 4])
print find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
print find_max_min([4, 4, 4, 4])