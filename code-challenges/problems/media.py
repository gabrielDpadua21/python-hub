class Solution:

    def media(self, number1, number2):
        PESO_1 = 3.5
        PESO_2 = 7.5
        media = (number1 * PESO_1 + number2 * PESO_2) / (PESO_1 + PESO_2)
        return f'MEDIA = {media:.5f}'
