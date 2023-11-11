from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [x + y for x, y in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
        return Polynomial(result)

    def __call__(self, param):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (param ** i)
        return result


poly1 = Polynomial([3, 7, 0, -9, 2])
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
poly3 = poly1 + poly2
print(poly3)


class UnsignedBinaryInteger:
    def __init__(self, num_str):

        self.num_str = num_str

    def decimal(self):
        result = 0
        lst = []
        length = len(self.num_str)

        for i in range(length-1, -1, -1):
            lst.append(int(self.num_str[i]))

        for i in range(length):
            print(lst[i] * (2 ** i))
            result += lst[i] * (2 ** i)

        return result

    def __lt__(self, other):
        return self.decimal() < other.decimal

    def __gt__(self, other):
        return self.decimal() > other.decimal

    def __eq__(self, other):
        return self.decimal() == other.decimal

    def is_twos_power(self):
        return  self.num_str.count('1') == 1

    def largest_twos_power(self):
        result = self.num_str[0] * (2 ** (len(self.num_str) - 1))
        return

    def __repr__(self):
        result = '0b'
        result += self.num_str
        return(result)

n = UnsignedBinaryInteger('1101')
print(n)


