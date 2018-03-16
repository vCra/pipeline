from enum import Enum


class Volume(object):

    class ReadModes(Enum):
        ReadWrite = "rw"
        ReadOnly = "ro"

    host_location = None
    container_location = None
    container_mode = None

    def __init__(self, host_location, container_location, container_mode=ReadModes.ReadOnly):
        self.host_location = host_location
        self.container_location = container_location
        self.container_mode = container_mode

    def as_dict(self):
        return {self.host_location: {"bind": self.container_location, "mode": self.container_mode.value}}

