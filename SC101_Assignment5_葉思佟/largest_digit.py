"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

answer = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The number that we enter.
	:return:
	"""
	find_largest_digit_helper(n, 0)
	return answer

def find_largest_digit_helper(n, current_high):
	global answer

	if n == 0:
		answer = current_high 		# The highest digit we are looking for, save it as an answer

	else:
		n = abs(n) 					# Make it the positive number
		single_number = n % 10 		# Use modulus to get each digit
		n = n // 10 				# Use floor division to remove the last digit

		if single_number > current_high:
			current_high = single_number

		find_largest_digit_helper(n, current_high)
		return answer




if __name__ == '__main__':
	main()
