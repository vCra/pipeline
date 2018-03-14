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
    command_list = []       # List of commands that will get loaded into the command manager

    def __init__(self, stage, config):
        self.stage = stage              # The stage this module is being called from
        self.user_config = config       # The config that the stage gave this module - i.e. from the .pipeline file
        self.volume_manager = VolumeManager(volumes=self.get_volumes())     # Manages the volume for a volume
        super(Module, self).__init__()

    def get_config(self):
        return {**self.config, **self.volume_manager.as_dict()}

    def get_volumes(self):
        """
        Gets the volumes used for this module
        :return:
        """
        return [Volume("workspace", "/code", Volume.ReadModes.ReadOnly), ]


    def run(self):
        self.job_manager = JobManager(self)
        self.job_manager.execute_all()




