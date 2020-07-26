from devices.logicdevice import LogicDevice


class Wire(LogicDevice):
    def do(self, *args) -> tuple:
        return args