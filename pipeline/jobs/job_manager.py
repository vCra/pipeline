from multiprocessing.pool import Pool
from random import random

from pipeline.jobs.configuration.config_manager import ConfigManager
from pipeline.jobs.job import Job


class JobManager(object):

    jobs = []
    module = None
    config_manager = None
    job_class = Job

    def __init__(self, module):
        self.module = module
        self.jobs = []

    def create_jobs(self):
        """
        Creates jobs from the config manager
        :return:
        """

        # def gen_job_name(v_config):
        #     """
        #     Generate a name for a matrix job, based on the matrix configuration
        #     :param v_config: The matrix job vertex
        #     :return:
        #     """
        #     from slugify import slugify
        #     return slugify(self.module.name+str(list(v_config.values())))

        self.config_manager = ConfigManager(
            self.module,
            self.module.stage.pipeline.global_config,
            self.module.user_config,
            self.module.stage.matrix
        )

        for job_config in self.config_manager.get_job_configs():
            self.jobs.append(
                self.job_class(job_config, self.module.stage.pipeline.docker)
            )

    def execute_all(self):  # TODO
        for job in self.jobs:
                job.start()

        for job in self.jobs:
            job.join()
