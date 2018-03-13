import yaml


class YAMLReader(object):
    file = None

    def __init__(self, file):
        """
        A parser for the YAML File
        :param file: a file object (with yaml in) to read
        """
        self.file = file
        self.file_reader = open(self.file)

    def load_stages(self):
        return yaml.load(self.file_reader)["stages"]
