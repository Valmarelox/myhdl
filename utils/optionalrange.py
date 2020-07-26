from typing import Optional


class OptionalRange:
    def __init__(self, a: Optional[int], b: Optional[int]):
        self.a = a
        self.b = b

    def __contains__(self, value):
        state = True
        if self.a:
            state &= (value >= self.a)
        if self.b:
            state &= (value <= self.b)

        return state




