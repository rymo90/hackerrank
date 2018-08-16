import itertools


class Difference:
    def __init__(self, a):
        self.__element = a
        self.maximum = 0

    def computeDifference(self):

        for a, b in itertools.combinations(self.__element, 2):
            if abs(a-b) > self.maximum:
                self.maximum = abs(a-b)

    def maximumDifference(self):
        return self.maximum


n = int(input())
a = [int(i) for i in input().split()]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference())
