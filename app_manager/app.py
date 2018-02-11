from os.path import expanduser


class App(object):
    def __init__(self, name, root, start_command, setup_commands):
        self.name = name
        self.root = expanduser(root)
        self.start_command = start_command
        self.setup_commands = setup_commands
