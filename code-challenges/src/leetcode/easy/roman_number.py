roman_value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

sub_values = ['IV', 'IX', 'XC', 'XL', 'CD', 'CM']

class RomanNumber:

    def romanToInt01(self, s: str) -> int:
        sum_values = 0
        letter_before = ''
        for letter in reversed(s):
            sum_values += roman_value[letter]
            if f"{letter}{letter_before}" in sub_values:
                sum_values -= roman_value[letter] + roman_value[letter_before]
                sum_values += roman_value[letter_before] - roman_value[letter]
            letter_before = letter
        return sum_values

    def romanToInt02(self, s: str) -> int:
        roman_int = 0

        for index, value in enumerate(s):
            if len(s) > index + 1 and roman_value[value] < roman_value[s[index + 1]]:
                roman_int -= roman_value[value]
            else:
                roman_int += roman_value[value]


        return roman_int
