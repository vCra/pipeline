class Configuration(object):
    """
    A configuration for a runnable docker job.
    """
    name = None
    image = None
    command = None
    auto_remove = None
    detach = None
    entrypoint = None
    environment = None
    hostname = None
    init = None
    log_config = None
    ports = None
    stream = None
    volumes = None
    working_dir = None

    extra = {}

    def __init__(self, **dictionary):
        """Constructor"""
        self._add_keys(**dictionary)

    def _add_keys(self, **dictionary):
        for key in dictionary:
            if key in dir(self):
                setattr(self, key, dictionary[key])
            else:
                print(key)

    def as_dict(self):
        return vars(self)

