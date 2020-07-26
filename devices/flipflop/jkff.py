from devices.flipflop.clockbasedlogicdevice import ClockBasedLogicDevice


class JKFF(ClockBasedLogicDevice):
    def do(self, j, k) -> tuple:
        self.next_state = (j and self.state) or (k and not self.state)
        return (self.state, not self.state)