from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class Not(LogicDevice):
    INPUTS_COUNT = OptionalRange(1, 1)
    OUTPUTS_COUNT = OptionalRange(1, 1)

    def __init__(self, inputs, outputs):
        super(Not, self).__init__(inputs, outputs)

    def do(self, input) -> tuple:
        return (not input,)

    def __repr__(self):
        return '!{0}'.format(self.inputs[0])


