from base_utils import BasedNumber
from devices import LogicDevice
from utils.bit import Bits
from utils.optionalrange import OptionalRange


class Decoder(LogicDevice):
    INPUTS_COUNT = OptionalRange(1, None)
    OUTPUTS_COUNT = OptionalRange(1, None)

    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)
        assert (2 ** len(inputs)) == len(outputs)

    def do(self, *args: Bits):
        binary_input = ''.join(map(lambda x: '1' if x else '0', args[::-1]))
        decoded = BasedNumber(2)(binary_input).to_base(10)
        return (False,) * decoded + (True,) + (False,) * (len(self.outputs) - decoded - 1)