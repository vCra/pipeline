from pipeline.jobs.matrix import MatrixManager


class ConfigManager(object):

    global_config = None  # The configuration for the whole pipeline
    module_config = None  # The configuration for the specific module
    user_config = None    # The configuration provided by the user
    matrix_manager = None

    job_configs = []

    #  Should the default (i.e. non matrix generated) configuration be added as a job?
    #  Ignored if no matrix is in use
    include_non_matrix_build = False

    def __init__(self, global_config, module_config, matrix=None):
        self.global_config = global_config
        self.module_config = module_config
        self.matrix_manager = MatrixManager(matrix) if matrix else None

    def set_matrix(self, matrix):
        self.matrix_manager = matrix

    def get_config(self, matrix_config=None):
        if matrix_config is None:
            matrix_config = {}
        from pipeline.jobs.configuration.configuration import Configuration
        return Configuration(**{**self.global_config, **self.module_config, **self.user_config, **matrix_config})

    def gen_matrix_config(self):
        for job_config in self.matrix_manager.get_vertices():
            self.job_configs.append(self.get_config(matrix_config=job_config))

    def gen_all_config(self):
        self.job_configs = []
        if self.matrix_manager:
            self.gen_matrix_config()
            if not self.include_non_matrix_build:
                return None
        self.job_configs.append(self.get_config())
