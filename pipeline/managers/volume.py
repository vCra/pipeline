import shutil
from enum import Enum

import os

from pipeline.managers.manager import Manager


class Volume(object):

    class ReadModes(Enum):
        ReadWrite = "rw"
        ReadOnly = "ro"

    def __init__(self,
                 host_location,
                 container_location,
                 container_mode=ReadModes.ReadOnly):
        self.host_location = host_location
        self.container_location = container_location
        self.container_mode = container_mode

    def as_dict(self):
        return {self.host_location: {"bind": self.container_location, "mode": self.container_mode.value}}


class VolumeManager(Manager):

    def update_config(self, configuration) -> dict:

        # Get workdir for project
        # Get project location - includes folders such as workspaces, logs, output ect
        # Create folder for job if we want it separate from the default workspace
        # Create workspace volume

        workspace_location = configuration.pop("workspace")
        project_folders = configuration.pop("project_location")

        create_workspace = configuration.get("uws")

        if create_workspace:
            workspaces_dir_location = configuration["workspaces_folder_location"]
            workspace_location = os.path.join(workspaces_dir_location, configuration)
            shutil.copytree(workspace_location, workspace_location)
            configuration.update({"workspace": workspace_location})

        vol = Volume(workspace_location, "/code", Volume.ReadModes.ReadWrite)

        volumes = configuration.get("volumes", {})
        volumes.update(**vol.as_dict())
        configuration.update({"volumes": volumes})

        return super().update_config(configuration)


