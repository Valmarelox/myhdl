from devices.flipflop.clockbasedlogicdevice import ClockBasedLogicDevice


class DFF(ClockBasedLogicDevice):
    def do(self, arg) -> tuple:
        self.next_state = arg
        return (self.state,)