from random import random

from pipeline.jobs.configuration.config_manager import ConfigManager
from pipeline.jobs.job import Job


class JobManager(object):

    jobs = []
    module = None
    config = None
    job_class = Job

    def __init__(self, module):
        self.module = module
        self.jobs = []

    def create_jobs(self):
        """
        Creates jobs from the config manager
        :return:
        """

        def gen_job_name(v_config):
            """
            Generate a name for a matrix job, based on the matrix configuration
            :param v_config: The matrix job vertex
            :return:
            """
            from slugify import slugify
            return slugify(self.module.name+str(list(v_config.values())))

        self.config = ConfigManager(
            self.module.stage.pipeline.global_config,
            self.module.config,
            self.module.user_config,
            self.module.stage.matrix
        )

        self.config.gen_all_config()
        for config in self.config.job_configs:
            config.name = config.name + str(random())
            self.jobs.append(
                self.job_class(config, self.module.stage.pipeline.docker)
            )

    def execute_all(self):
        for job in self.jobs:
            job.begin()
