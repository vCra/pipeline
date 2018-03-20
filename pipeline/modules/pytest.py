from pipeline.module import Module


class PytestCIModule(Module):
    config = {
        "image": "python:3",
        "command": "pytest",
    }

    def gen_config(self, config):

        try:
            py = config.pop("python_version")
            config["image"] = "python:" + str(py)
        except KeyError:
            pass

        try:
            requirements = config.pop("requirements_command")
            self.command_manager.add_command(requirements, 1)
        except KeyError:
            pass

        config = super(PytestCIModule, self).gen_config(config)

        return config

pipeline_ci_module = PytestCIModule
