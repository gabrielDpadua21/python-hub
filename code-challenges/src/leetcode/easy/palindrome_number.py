

class PalindromeNumber:

	def solution01(self, number: int) -> bool:
		return str(number) == "".join(reversed(str(number)))

	def solution02(self, number: int) -> bool:
		if number < 0: return False

		reversed_num = 0
		temp = number

		while temp != 0:
			digit = temp % 10
			reversed_num = reversed_num * 10 + digit
			temp //= 10

		return reversed_num == number 