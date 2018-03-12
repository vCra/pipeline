from pluginbase import PluginBase
from transitions import Machine


class Stage(object):
    """
    A stage of the pipeline
    """
    states = ['starting', 'running', 'success', 'failed', 'error', 'aborted', ]

    name = None
    module = None
    matrix = None
    jobs = None
    config = None

    def __init__(self, name, module,  *args, **kwargs):
        self.machine = Machine(model=self, states=self.states, initial='starting')
        self.name = name
        self.modules = module
        self.create_state_transactions()
        self.post_init()


    def load_module(self):
        plugin_base = PluginBase(package='pipeline.modules')
        modules_home = plugin_base.make_plugin_source(
            searchpath=['./modules', ]
        )


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


