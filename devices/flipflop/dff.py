from devices.flipflop.clockbasedlogicdevice import ClockBasedLogicDevice


class DFF(ClockBasedLogicDevice):
    def do(self, arg) -> tuple:
        self._next_state = arg
        return super().do()