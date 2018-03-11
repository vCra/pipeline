import os
import shutil

import sys

import itertools
import yaml

from git import Repo
from pluginbase import PluginBase
from slugify import slugify

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

def setup_module_finder():
    plugin_base = PluginBase(package='pipeline.modules')
    global modules
    modules = plugin_base.make_plugin_source(
        searchpath=['./modules', ]
    )

def setup_workspace():
    shutil.rmtree(project_location, ignore_errors=True)
    os.makedirs(workspace_location, exist_ok=True)
    os.mkdir(log_location)
    os.mkdir(output_location)


def clone():
    Repo.clone_from(git_url, workspace_location)
    print("Cloned from "+ git_url)


def fake_pipeline():
    open(pipeline_file, "w+").writelines(open("../.pipeline").readlines())


def load_stages():
    global yaml_data
    yaml_data = yaml.load(open(pipeline_file))


def load_module(module_name):
     return modules.load_plugin(module_name)


def setup_docker():
    import docker
    return docker.from_env()


def gen_matrix_builds(matrix):
    names = sorted(matrix)
    combinations = itertools.product(*(matrix[Name] for Name in names))
    jobs = []
    for c in combinations:
        d = {}
        for i in range(len(names)):
            d.update({names[i]:c[i]})
        jobs.append(d)
    return jobs

def matrix_job(job, module):
    job_name = slugify(stage["name"]+str(list(job.values())))
    print("Starting " + job_name)
    sys.stdout.flush()
    exit = module.run(
        docker=docker,
        workspace=workspace_location,
        output=output_location,
        config=dict(config, **job)
    )
    if exit is not 0:
        print("FAILURE - EXIT CODE " + str(exit))
    else:
        print("Job " + job_name + " has finished successfully!")

if __name__ == "__main__":
    setup_module_finder()
    setup_workspace()
    clone()
    fake_pipeline()
    load_stages()
    docker = setup_docker()

    for stage in yaml_data["stages"]:
        print("Running Stage: " + stage["name"])
        config = stage["module"].get("config", {})
        matrix = stage.get("matrix", config)
        module = load_module(stage["module"]["name"])

        if matrix:
            jobs = gen_matrix_builds(matrix)
            for job in jobs:
                matrix_job(job, module)

        else:
            exit = module.run(docker=docker, workspace=workspace_location, output=output_location, config=config)
            if exit is not 0:
                print("FAILURE - EXIT CODE " + str(exit))