import os
import shutil

from git import Repo
from pipeline import Pipeline

pipeline_location = "/pipeline"
project_name = "test"
workspace_folder = "workspace"
output_folder = "output"
log_folder = "logs"
git_url = "https://github.com/django/daphne.git"

project_location = os.path.join(pipeline_location, project_name)
workspace_location = os.path.join(project_location, workspace_folder)
output_location = os.path.join(project_location, output_folder)
log_location = os.path.join(project_location, log_folder)
pipeline_file = os.path.join(workspace_location, ".pipeline")

yaml_data = None
modules = None


def setup_workspace():
    shutil.rmtree(project_location, ignore_errors=True)
    os.makedirs(workspace_location, exist_ok=True)
    os.mkdir(log_location)
    os.mkdir(output_location)


def clone():
    Repo.clone_from(git_url, workspace_location)


def fake_pipeline():
    open(pipeline_file, "w+").writelines(open("../.pipeline").readlines())


def setup_docker():
    import docker
    return docker.from_env()


def test():
    setup_workspace()
    clone()
    fake_pipeline()


if __name__ == "__main__":
    test()
    docker_client = setup_docker()
    pipeline = Pipeline(pipeline_file, docker_client)
