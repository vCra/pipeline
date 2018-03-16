from pipeline.module import Module


class PytestCIModule(Module):
    config = {
        "image": "python:3"
    }


pipeline_ci_module = PytestCIModule
