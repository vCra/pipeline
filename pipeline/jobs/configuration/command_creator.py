class CommandCreator(object):
    """
    Stores commands in a tuple in the format (priority, command)
    """
    commands = None

    def __init__(self, command=""):
        self.commands = []
        self.add_command(command)

    def add_command(self, command, priority=5):
        self.commands.append((priority, command or ""))

    def set_command(self, command, priority=5):
        self.commands.append((priority, command or ""))

    def set_commands(self, commands):
        self.commands = commands

    def get_commands_list(self):
        return sorted(self.commands)

    def get_command(self):
        if self.commands:
            return '/bin/sh -c '.join([command[1] for command in sorted(self.commands)])
        return None

    def as_dict(self):
        if self.get_command():
            return {"command": self.get_command()}
        return {}
