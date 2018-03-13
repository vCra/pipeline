import os

from pipeline.module import Module


def run(**kwargs):
    docker = kwargs["docker"]
    workspace = kwargs["workspace"]

    volume = {
        workspace: {'bind': "/code", 'mode': 'ro'}
    }
    container = docker.containers.run("eeacms/flake8", detach=True, volumes=volume)
    exit_code = container.wait()["StatusCode"]
    flake8_report = os.path.join(kwargs["output"], "flake8.txt")
    with open(flake8_report, "w+") as file:
        for line in container.logs(stream=True):
            file.writelines(line.decode('ascii'))
    return exit_code


class Flake8CIModule(Module):
    def run(self):
        print("Hello")
        print(self.volume_manager.as_dict())
        return 0


pipeline_ci_module = Flake8CIModule
