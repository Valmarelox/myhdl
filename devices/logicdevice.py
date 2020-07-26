from abc import abstractmethod
from collections import Sequence
from typing import Union

from utils.basevariable import BaseVariable
from utils.optionalrange import OptionalRange


class LogicDevice:
    INPUTS_COUNT = OptionalRange(None, None)
    OUTPUTS_COUNT = OptionalRange(None, None)

    def __init__(self, inputs: Union[Sequence, str] = tuple(), outputs: Union[Sequence, str] = tuple()):
        if isinstance(inputs, (str, BaseVariable)):
            inputs = (inputs,)
        if isinstance(outputs, (str, BaseVariable)):
            outputs = (outputs,)
        self.inputs = tuple(str(x) for x in inputs)
        self.outputs = tuple(str(x) for x in outputs)
        assert len(self.inputs) in self.INPUTS_COUNT
        assert len(self.outputs) in self.OUTPUTS_COUNT, self.outputs

    @abstractmethod
    def do(self, *args: tuple) -> tuple:
        raise NotImplementedError()

