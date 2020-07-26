from devices import LogicDevice
from devices.basic import Xor, Not, And
from utils.basevariable import BaseVariable


class Expression(BaseVariable):
    def __init__(self, value: LogicDevice):
        self.value = value


class Variable(BaseVariable):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __xor__(self, other):
        return Xor([self, other], Variable('xor_{0}_{1}'.format(self, other)))

    def __invert__(self):
        return Not(self, Variable('not_{0}'.format(self)))

    def __and__(self, other):
        return And([self, other], Variable('and_{0}_{1}'.format(self, other)))
