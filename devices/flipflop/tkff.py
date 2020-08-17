from devices.flipflop.clockbasedlogicdevice import ClockBasedLogicDevice


class TKFF(ClockBasedLogicDevice):
    def do(self, t) -> tuple:
        self.next_state = (t ^ self.state)
        return super().do()