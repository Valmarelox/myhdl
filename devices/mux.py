from devices import LogicDevice


class Mux(LogicDevice):
    def __init__(self, size, inputs, outputs):
        super(Mux, self).__init__(inputs, outputs)
        self.size = size

    def do(self, *args):
        selection, inputs = args[:self.size], args[self.size:]
        sel = int(''.join(map(lambda x: '1' if x else '0', selection))[::-1], 2)
        return (inputs[sel], )
