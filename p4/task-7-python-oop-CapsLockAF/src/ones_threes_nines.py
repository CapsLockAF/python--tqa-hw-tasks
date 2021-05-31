class OnesThreesNines:
    def __init__(self, num):
        self.num = num
        self.ones = self.__get_x(1)
        self.nines = self.__get_x(9)
        self.threes = self.__get_x(3)

    def __get_x(self, x):
        n = self.num
        if x == 1:
            return n
        c = 0
        while n >= x:
            n -= x
            c += 1
        return c
