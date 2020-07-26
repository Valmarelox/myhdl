from itertools import count
import string

DIGITS = string.digits + string.ascii_lowercase

def base_generator(base):
    for exp in count(0):
        yield base ** exp
        exp += 1


def BasedNumber(base):
    class BasedNumber:
        BASE = base

        def __init__(self, number):
            assert self.validate(number)
            self.number = number

        @classmethod
        def validate(cls, number):
            return all(0 <= DIGITS.index(x) < cls.BASE for x in str(number))

        @classmethod
        def _to_base10(cls, number):
            return sum(map(lambda b: b[0] * b[1], zip(map(lambda x: DIGITS.index(x), str(number)[::-1]), base_generator(cls.BASE))))

        def to_base(self, new_base):
            base10 = self._to_base10(self.number)
            if new_base == 10:
                return base10
            ng_number = []
            while base10 != 0:
                ng_number.append(DIGITS[base10 % new_base])
                base10 //= new_base
            return ''.join(ng_number[::-1])

        def __repr__(self):
            return str(self.number)

    return BasedNumber


print(BasedNumber(9)(87631254).to_base(3))