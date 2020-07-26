from itertools import product
from typing import Dict, List

from prettytable import PrettyTable

from devices.flipflop import ClockBasedLogicDevice
from utils.bit import Bit


class Circuit(ClockBasedLogicDevice):
    def __init__(self, inputs, outputs, devices):
        super().__init__(inputs, outputs)
        self.devices = devices

    def __repr__(self):
        pass

    def cycle_state(self):
        for dev in self.devices:
            if isinstance(dev, ClockBasedLogicDevice):
                dev.cycle_state()

    def generator(self, values: Dict[str, Bit]):
        while values:
            outputs = self.do(values)
            inputs: Dict[str, Bit] = (yield outputs)
            self.cycle_state()
            values = inputs

    def do(self, values: Dict[str, Bit]):
        devs = list(self.devices)
        values.update({'1': True, '0': False})
        last_size = len(devs)
        while devs:
            for device in devs:
                if set(device.inputs).issubset(tuple(values.keys())):
                    args = [values[input] for input in device.inputs]
                    outputs = {x: y for (x, y) in zip(device.outputs, device.do(*args))}
                    values.update(outputs)
                    devs.remove(device)
            assert last_size != len(devs)
        print(self.outputs)
        return {x: values[x] for x in self.outputs}

    def all_outputs(self) -> List:
        inputs: List = self.inputs
        outputs = []
        for table in product((False, True), repeat=len(inputs)):
            outputs.append((table, self.do(dict(zip(inputs, table)))))
        return outputs

    def build_table(self) -> PrettyTable:
        p = PrettyTable()
        t = self.all_outputs()
        p.field_names = self.inputs + self.outputs
        for res in t:
            a, b = res[0], res[1]
            print(a, b)
            p.add_row(list(map(int, a + tuple(b[key] for key in self.outputs))))
        return p

    def __eq__(self, other) -> bool:
        # TODO: Must compare states as well
        return self.all_outputs() == other.all_outputs()


