from utils.bit import Bits
from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class And(LogicDevice):
    INPUTS_COUNT = OptionalRange(1, None)
    OUTPUTS_COUNT = OptionalRange(1, 1)

    def do(self, *args: Bits) -> tuple:
        return (all(args),)

    def __repr__(self):
        return '(' + '*'.join(self.inputs) + ')'