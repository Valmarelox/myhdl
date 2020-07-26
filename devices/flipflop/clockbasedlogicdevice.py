from devices.logicdevice import LogicDevice


class ClockBasedLogicDevice(LogicDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = 0
        self.next_state = 0

    def cycle_state(self):
        self.state = self.next_state