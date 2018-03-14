<<<<<<< HEAD
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
=======
from pluginbase import PluginBase
from transitions import Machine


class Stage(object):
    """
    A stage of the pipeline
    """
    stages = ['starting', 'running', 'success', 'failed', 'error', 'aborted', ]

    name = None
    modules = None
    matrix = None
    jobs = None
    config = None

    def __init__(self, name, module,  *args, **kwargs):
        self.machine = Machine(model=self, states=self.stages, initial='starting')
        self.name = name
        self.modules = module
        self.create_state_transactions()
        self.post_init()


    def load_modules(self, modules):
        plugin_base = PluginBase(package='pipeline.modules')
        modules_home = plugin_base.make_plugin_source(
            searchpath=['./modules', ]
        )
        for module in modules:
            self.modules.append(load_module(stage["module"]["name"])
    def create_state_transactions(self):
        self.machine.add_transition('post_init', 'starting', 'running')
        self.machine.add_transition('success', 'running', 'success')
        self.machine.add_transition('failure', 'running', 'failed')
        self.machine.add_transition('error', 'running', 'error')
        self.machine.add_transition('abort', '*', 'aborted')

    def start(self):
        print("Running Stage: " + self.name)

        if matrix:
            jobs = gen_matrix_builds(matrix)
            for job in jobs:
                matrix_job(job, module)

        else:
            sys.stdout = open(os.path.join(log_location, slugify(stage["name"])), 'w')
            exit = module.run(docker=docker, workspace=workspace_location, output=output_location, config=config)
            sys.stdout = sys.__stdout__
            if exit is not 0:
                print("FAILURE - EXIT CODE " + str(exit))


>>>>>>> 0d84f86... Add pipeline files
