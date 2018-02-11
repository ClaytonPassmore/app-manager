import os
from config import config
from utils import execute

import tmux


class Project(object):
    def __init__(self, name):
        self.name = name

    def setup(self):
        os.chdir(config.get_directory(self.name))
        for command in config.get_setup_commands(self.name):
            execute(command)

    def start(self, start_attached=False):
        os.chdir(config.get_directory(self.name))
        tmux.new_session(self.name, config.get_start_command(self.name), attached=start_attached)

    def stop(self):
        tmux.send_keys(self.name, 'C-c')

    def attach(self):
        tmux.attach(self.name)
