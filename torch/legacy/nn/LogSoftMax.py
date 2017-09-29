import torch
from .Module import Module


class LogSoftMax(Module):

    def updateOutput(self, input):
        self._backend.LogSoftMax_updateOutput(
            self._backend.library_state,
            input,
            self.output,
            0 if input.dim() == 1 or input.dim() == 3 else 1
        )
        return self.output

    def updateGradInput(self, input, gradOutput):
        self._backend.LogSoftMax_updateGradInput(
            self._backend.library_state,
            input,
            gradOutput,
            self.gradInput,
            self.output,
            0 if input.dim() == 1 or input.dim() == 3 else 1
        )
        return self.gradInput
