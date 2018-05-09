from pipeline.jobs.matrix import MatrixManager


class ConfigManager(object):

    # TODO: IDEAS

    """
      - Get config from subclassed module - override method?
      - store reference to module rather than module config on init - be able to call module.get_config(), which module
        creator can override for whatever reason - e.g. config generation etc...
      - Handle global config better somehow?
    """

    global_config = None   # The configuration for the whole pipeline
    user_config = None     # The configuration provided by the user
    module = None          # The module that this configuration is for
    matrix_manager = None  # The matrix used to generate config on a per job basis

    job_configs = []

    #  Should the default (i.e. non matrix generated) configuration be added as a job?
    #  Ignored if no matrix is in use
    include_non_matrix_build = False

    def __init__(self, module, global_config, user_config, matrix=None):
        self.global_config = global_config
        # self.module_config = module_config
        self.module = module
        self.user_config = user_config
        self.matrix_manager = MatrixManager(matrix) if matrix else None

    def set_matrix(self, matrix):
        self.matrix_manager = matrix

    def get_config(self, matrix_config=None):
        if matrix_config is None:
            matrix_config = {}
        from pipeline.jobs.configuration.configuration_docker import Configuration
        config_dict = {**self.global_config, **self.module.config, **self.user_config, **matrix_config}

        return Configuration(**self.module.gen_config(config_dict))

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

    # TODO: Convert into generator
    def get_job_configs(self):
        self.gen_all_config()
        return self.job_configs

