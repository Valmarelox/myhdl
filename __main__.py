from circuit import Circuit
from devices.basic import Xor, Wire, Not, And, Or, Nor
from devices.decoder import Decoder
from devices.flipflop import DFF, JKFF
from devices.mux import Mux
from utils.variable import Variable

c = Circuit(inputs=['x0', 'x1', 'y'], outputs=['a4', 'a3', 'a2', 'a1', 'a0'], devices=[
    Xor([Variable('x1'), 'y'], 'a0'),
    Wire('0', 'a1'),
    Not('x0', 'not_x0'),
    And(['not_x0', 'x1', 'y'], 'half_a2_0'),
    Not('x1', 'not_x1'),
    Not('y', 'not_y'),
    And(['x0', 'not_x1', 'not_y'], 'half_a2_1'),
    Or(['half_a2_0', 'half_a2_1'], 'a2'),
    Xor(['x1', 'y'], 'xor_x1_y'),
    And(['x0', 'xor_x1_y'], 'a3'),
    And(['x0', 'x1', 'y'], 'a4')
])
print(c.build_table())
print(c == c)

v = Variable('v')
u = Variable('u')
print(v ^ u)
c = Circuit(inputs=['x','y'], outputs=['z'], devices=[
    Decoder(['x','y'], outputs=['a0', 'a1', 'a2', 'a3']),
    DFF('a0', 'A'),
    Not('A', 'K'),
    Nor(['a2', 'a3'], 'J'),
    JKFF(['J', 'K'], outputs=['B', 'nB']),
    Xor(['nB', 'A', 'y'], 'z')
])
print(c.build_table())

#c = Circuit(['w','x','y','z'], outputs='out', devices=[
#    Not('y', 'ny'),
#    Or(['x', 'z'], 'xz'),
#    Mux(2, ['w', 'ny', 'ny', 'ny', 'x', 'xz'], 'out')
#])
#print(c.build_table())