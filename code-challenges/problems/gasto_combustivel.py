class Solution:

    def fuel_spent(self, time, speed):
        distance = time * speed
        fuel = distance / 12
        return f'{fuel:.3f}'