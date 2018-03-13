from pipeline.module import Module


def run(config, **kwargs):
    print("Starting PyTest")
    docker = kwargs["docker"]
    workspace = kwargs["workspace"]
    python_image = config.get("language_version", "python:3")
    requirements_required = config.get("requirements_required", True)
    requirements_command = config.get("requirements_command", "pip install -r requirements.txt")

    environment = config.get("environment", "").split(", ")


    run_command = config.get("pytest_command", "pytest")
    volume = {
        workspace: {'bind': "/code", 'mode': 'rw'}
    }
    if requirements_required:
        command = "/bin/sh -c '"+requirements_command+";"+run_command+"'"
    else:
        command = run_command
    container = docker.containers.run(python_image, detach=True, volumes=volume, working_dir="/code", command=command, environment=environment)
    exit_code = container.wait()["StatusCode"]
    for line in container.logs(stream=True):
        print(line.decode('ascii'))
    return exit_code


class PytestCIModule(Module):
    def run(self):
        print("This is pytest!")

pipeline_ci_module = PytestCIModule