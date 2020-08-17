from devices.flipflop.clockbasedlogicdevice import ClockBasedLogicDevice


class JKFF(ClockBasedLogicDevice):
    def do(self, j, k) -> tuple:
        self._next_state = (j and self._state) or (k and not self._state)
        return super().do()