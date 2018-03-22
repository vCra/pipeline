class Stage(object):
    module = None
    name = ""
    pipeline = None
    matrix = None

    def __init__(self, config, pipeline):
        self.name = config["name"]
        self.pipeline = pipeline
        self.load_module(config["module"])
        self.load_matrix(config)

    def get_stage_status(self):
        return self.module.status

    def load_matrix(self, config):
        try:
            self.matrix = config["matrix"]
        except KeyError:
            self.matrix = None

    def load_module(self, module_data):
        module = self.pipeline.modules.load_plugin(module_data["name"])
        self.module = module.pipeline_ci_module(self, config=module_data)

    def run(self):
        self.module.run()
