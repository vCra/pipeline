from pipeline.modules.module import StarterModule


class PytestCIModule(StarterModule):
    config = {
        "image": "python:3",
    }
    command = "pytest"

    def gen_config(self, config):

        try:
            py = config.pop("python_version")
            config["image"] = "python:" + str(py)
        except KeyError:
            pass

        try:
            requirements = config.pop("requirements_command")

        except KeyError:
            pass

        config = super(PytestCIModule, self).gen_config(config)

        return config

pipeline_ci_module = PytestCIModule
