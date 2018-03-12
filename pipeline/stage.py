class Stage(object):
    def __init__(self):
        return super(Stage, self).__init__()

    module = None
    settings = {}

    def run_module(self):
        pass

    def get_stage_status(self):
        return self.module.status

