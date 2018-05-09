from pipeline.jobs.job_manager import JobManager
from pipeline.managers.volume import VolumeManager


class BaseModuleMixin(object):
    pass


class ModuleConfigMixin(BaseModuleMixin):
    config = {}             # Settings specific to this module
    user_config = {}        # Settings provided by the user in the pipeline file

    def __init__(self, *args, **kwargs):
        super(ModuleConfigMixin, self).__init__()
        self.user_config = kwargs.pop("config")  # The config that the stage gave this module - i.e. from the
        # .pipeline file


class BaseModule(object):
    name = "Module"         # The user friendly name of this module
    stage = None            # The stage of the pipeline that this module is running in
    supported_configs = []  # List of possible configuration values, which can be used to configure tge

    def __init__(self, stage, *args, **kwargs):
        self.stage = stage              # The stage this module is being called from
        super(BaseModule, self).__init__(*args, **kwargs)

    def run(self):
        """
        Run the module's job
        """
        pass


class Module(BaseModule, ModuleConfigMixin):
    pass


class ManagerModule(Module):
    """
    Module that uses a manager to do things?
    """
    managers = {}           # List of managers used to generate per job configuration

    def get_managers(self):
        return self.managers

    def gen_config(self, config):
        """
        To be ran before a job is run - processes the jobs config, and
        """
        print()
        for manager_key, manager_value in self.get_managers().items():
            config.update(manager_value.update_config(config))
        return config


class JobBasedModule(ManagerModule):
    """
    Module for running job based tasks
    """
    def __init__(self, *args, **kwargs):
        super(JobBasedModule, self).__init__(*args, **kwargs)
        self.job_manager = JobManager(self)

    def run(self):
        """
        Create jobs within the job manager, and then run them
        :return:
        """
        self.job_manager.create_jobs()
        self.job_manager.execute_all()


class StarterModule(JobBasedModule):
    """
    A module including commonly used modules, for volumes, commands etc...
    """

    managers = {
        "volume_manager": VolumeManager()
    }