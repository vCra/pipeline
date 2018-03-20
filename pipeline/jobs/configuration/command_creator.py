from pipeline.utils.queue import UniquePriorityQueue


class CommandCreator(object):
    """
    Stores commands in a tuple in the format (priority, command)
    """
    commands = None

    def __init__(self, command=None):
        self.commands = UniquePriorityQueue()
        self.add_command(command)

    def add_command(self, command, priority=5):
        if command:
            self.commands.put((priority, command))

    def add_commands(self, commands):
        if commands:
            for command in commands:
                self.add_command(command)

    def get_command(self):
        command_string = '/bin/sh -c "'
        if self.commands.empty():
            return None
        while not self.commands.empty():
            command_string = command_string + self.commands.get() + " ; "
        return command_string + '"'

    def as_dict(self):
        if not self.commands.empty():
            return {"command": self.get_command()}
        return {}
