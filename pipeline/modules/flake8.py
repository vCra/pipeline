import os

from pipeline.module import Module


class Flake8CIModule(Module):
    def run(self):
        print("Hello")
        print(self.volume_manager.as_dict())
        return 0


pipeline_ci_module = Flake8CIModule
