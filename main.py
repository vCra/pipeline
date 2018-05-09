import os
import shutil

from pluginbase import PluginBase

from pipeline.pipeline import Pipeline

pipeline_location = "/pipeline"
project_name = "test"
workspace_folder = "workspaces/0"
output_folder = "output"
log_folder = "logs"

project_location = os.path.join(pipeline_location, project_name)
workspace_location = os.path.join(project_location, workspace_folder)
output_location = os.path.join(project_location, output_folder)
log_location = os.path.join(project_location, log_folder)
pipeline_file = os.path.join(workspace_location, ".pipeline")

yaml_data = None


plugin_base = PluginBase(package='pipeline.modules')
modules = plugin_base.make_plugin_source(
    searchpath=['./pipeline/modules', ]
)


def setup_workspace():
    os.makedirs(workspace_location, exist_ok=True)
    os.makedirs(log_location, exist_ok=True)
    os.makedirs(output_location, exist_ok=True)


def fake_pipeline():
    open(pipeline_file, "w+").writelines(open(".pipeline").readlines())


def setup_docker():
    import docker
    return docker.from_env()


def test():
    setup_workspace()
    fake_pipeline()


if __name__ == "__main__":
    test()
    docker_client = setup_docker()
    pipeline = Pipeline(pipeline_file, docker_client, modules)
