class PonderedMean:
    
    def solution(self, value1, value2, value3):
        mean = ((value1 * 2) + (value2 * 3) + (value3 * 5)) / 10;
        return 'MEDIA = ' + '%.1f' % mean
