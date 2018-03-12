class CommandCreator(object):
    """
    Stores commands in a tuple in the format (priority, command)
    """
    commands = []

    def __init__(self):
        super(CommandCreator, self).__init__()

    def add_command(self, command, priority=5):
        self.commands.append((priority, command))

    def set_commands(self, commands):
        self.commands = commands

    def get_commands_list(self):
        return sorted(self.commands)

    def get_command(self):
        if self.commands:
            return '/bin/sh -c '.join([command[1] for command in sorted(self.commands)])
        return None
