class SimpleMean:

    def solution(self, value1, value2):
        mean = ((value1 * 3.5) + (value2 * 7.5)) / 11
        return "MEDIA = " + "%.5f" % (mean)