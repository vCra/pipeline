from pipeline.module import Module


class PytestCIModule(Module):
    def run(self):
        print("Starting PyTest")
        super(PytestCIModule, self).run()


pipeline_ci_module = PytestCIModule
