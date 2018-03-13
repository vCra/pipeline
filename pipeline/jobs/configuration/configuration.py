class Configuration(object):
    """
    A configuration for a job
    """
    name = None
    image = None
    command = None
    auto_remove = None
    detach = None
    entrypoint = None
    enviroment = None
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
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def as_dict(self):
        return vars(self)

