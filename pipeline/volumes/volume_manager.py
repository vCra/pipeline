class VolumeManager(object):

    local_volumes = []

    def __init__(self, volumes=[]):
        self.bulk_add_volumes(volumes)

    def bulk_add_volumes(self, volumes):
        for volume in volumes:
            self.add_volume(volume)

    def add_volume(self, volume):
        self.local_volumes.append(volume)

    def get_volumes(self):
        return self.local_volumes

    def as_dict(self):
        return {"volumes": self.get_volumes()}


