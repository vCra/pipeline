from pipeline.stage import Stage
from pipeline.yaml_reader import YAMLReader


class Pipeline(object):
    job_id = 1
    modules = None
    stages = []
    pipeline = None
    docker = None
    global_config = {
        "detach": True,
        "project_location": "/pipeline/test/",
        "workspace": "/pipeline/test/workspaces/0",
        "workspaces_folder_location": "/pipeline/test/workspaces/"
    }

    def __init__(self, pipeline_file, docker_client, modules):
        self.docker = docker_client
        self.modules = modules
        yaml_stages = YAMLReader(pipeline_file).load_stages()
        for stage in yaml_stages:
            new_stage = Stage(stage, self)
            self.stages.append(new_stage)

        for stage in self.stages:
            stage.run()
        super(Pipeline, self).__init__()

