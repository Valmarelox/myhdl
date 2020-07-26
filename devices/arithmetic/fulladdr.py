from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class FullAddr(LogicDevice):
    INPUTS_COUNT = OptionalRange(3, 3)
    OUTPUTS_COUNT = OptionalRange(2, 2)

    def do(self, x, y, c) -> tuple:
        return (x ^ y ^ c, (x + y + c) >= 2)