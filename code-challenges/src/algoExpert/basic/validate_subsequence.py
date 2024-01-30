class ValidateSubsequence:

    def solution01(self, array, sequence):
        arrayIndex = 0
        sequenceIndex = 0

        while arrayIndex < len(array) and sequenceIndex < len(sequence):
            if sequence[sequenceIndex] == array[arrayIndex]:
                sequenceIndex += 1
            arrayIndex += 1

            if arrayIndex == len(array) and sequenceIndex < len(sequence):
                return False
            elif sequenceIndex == len(sequence) and arrayIndex > len(array):
                return False

        return True

    def solution02(self, array, sequence):
        arrayIndex = 0
        sequenceIndex = 0

        while arrayIndex < len(array) and sequenceIndex < len(sequence):
            if sequence[sequenceIndex] == array[arrayIndex]:
                sequenceIndex += 1
            arrayIndex += 1

        return sequenceIndex == len(sequence)

    def solution03(self, array, sequence):
        sequenceIndex = 0

        for value in array:
            if sequenceIndex == len(sequence):
                break
            if sequence[sequenceIndex] == value:
                sequenceIndex += 1

        return sequenceIndex == len(sequence)
