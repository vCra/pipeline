from docker.models.containers import Container

from pipeline.jobs.command_creator import CommandCreator


class Job(Container):
    name = ""
    commands = CommandCreator()
    module = None
    image = None
    client = None
    enviroment = {}

    def __init__(self, name, module, image, client, **kwargs):
        self.name = name
        self.module = module
        self.client = client

        super(Job, self).__init__()

    def pre_run(self):
        pass

    def post_run(self):
        pass

    def run(self, *args, **kwargs):

        self.client.run(
            image=self.image,
            command=self.commands.get_command(),
            enviroment=self.enviroment,

        )

