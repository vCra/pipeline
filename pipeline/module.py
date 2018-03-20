from pipeline.jobs.configuration.command_creator import CommandCreator
from pipeline.jobs.job_manager import JobManager
from pipeline.volumes.volume import Volume
from pipeline.volumes.volume_manager import VolumeManager


class Module(object):
    name = "Module"         # The user friendly name of this module
    config = {}             # Settings specific to this module
    user_config = {}        # Settings provided by the user in the pipeline file
    volume_manager = None   # Volume manager
    job_manager = None      # Job manager
    log_manager = None      # Log manager
    stage = None            # The stage of the pipeline that this module is running in
    command_manager = None  # Manager for the commands
    command = None          # Command to Run
    supported_configs = []  # List of possible configuration values, which can be used to configure tge

    def __init__(self, stage, config):
        self.stage = stage              # The stage this module is being called from
        self.user_config = config       # The config that the stage gave this module - i.e. from the .pipeline file
        self.job_manager = JobManager(self)
        self.command_manager = CommandCreator(self.command)
        self.volume_manager = VolumeManager(volumes=self.volumes)     # Manages the volume for a volume

    def gen_config(self, config):
        """
        To be ran before a job is run - processes the jobs config, and
        """
        config.update(self.command_manager.as_dict())
        config.update(self.volume_manager.as_dict())
        return config

    def get_config(self):
        return self.config

    @property
    def volumes(self):
        """
        Gets the volumes used for this module
        :return:
        """
        return [Volume("/pipeline/test/workspace/", "/code", Volume.ReadModes.ReadWrite), ]

    def run(self):
        self.job_manager.create_jobs()
        self.job_manager.execute_all()
