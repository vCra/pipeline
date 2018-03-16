from pipeline.stage import Stage
from pipeline.yaml_reader import YAMLReader


class Pipeline(object):
    modules = None
    stages = []
    pipeline = None
    docker = None
    global_config = {
        "detach": True
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

