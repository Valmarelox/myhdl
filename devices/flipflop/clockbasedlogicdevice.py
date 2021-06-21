from devices.logicdevice import LogicDevice
from utils.optionalrange import OptionalRange


class ClockBasedLogicDevice(LogicDevice):
    OUTPUTS_COUNT = OptionalRange(1, 2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state = 0
        self._next_state = 0

    def set_state(self, state):
        self._state = state

    def cycle_state(self):
        self._state = self._next_state

    def do(self) -> tuple:
        if len(self.outputs) == 2:
            return (self._state, not self._state)
        elif len(self.outputs) == 1:
            return (self._state, )
        else:
            assert False, len(self.outputs)

    def __repr__(self):
        return f'{type(self).__name__}: {self.outputs[0]} (t-1)'
