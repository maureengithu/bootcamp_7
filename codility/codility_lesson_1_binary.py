def solution(n):
	maxlength = 0
	currentlength = 0

	while n > 0:
		if n % 2 == 1:
			currentlength = 0
		else:
			currentlength += 1
		if currentlength > maxlength:
			maxlength = currentlength

		n //= 2 

print solution(1041)