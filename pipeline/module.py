class Module(object):

    matrix = None  # Matrix Manager
    config = {}    # Module Settings
    status = None  # Status Manager
    volume = None  # Volume manager
    jobs = None    # Job manager
    logs = None    # Log manager

    def __init__(self, module_name, module_config, module_matrix):

        super(Module, self).__init__()

    def run(self):
        # Run each job
