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
        super(Stage, self).__init__()

    def get_stage_status(self):
        return self.module.status

    def load_matrix(self, config):
        try:
            self.matrix = config["matrix"]
        except KeyError:
            self.matrix = None

    def load_module(self, module_data):
        module = self.pipeline.modules.load_plugin(module_data["name"])
        module_class = module.pipeline_ci_module
        self.module = module_class(self, module_data)

    def run(self):
        self.module.run()
