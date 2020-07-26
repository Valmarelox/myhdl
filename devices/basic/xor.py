from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class Xor(LogicDevice):
    INPUTS_COUNT = OptionalRange(1, None)
    OUTPUTS_COUNT = OptionalRange(1, 1)

    def do(self, *args: tuple) -> tuple:
        return (bool(sum(args) % 2),)