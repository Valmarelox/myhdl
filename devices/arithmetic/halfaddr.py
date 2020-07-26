from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class HalfAddr(LogicDevice):
    INPUTS_COUNT = OptionalRange(2, 2)
    OUTPUTS_COUNT = OptionalRange(2, 2)

    def do(self, x, y) -> tuple:
        return (x ^ y, x & y)