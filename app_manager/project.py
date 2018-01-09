import os
from config import config
from utils import execute


class Project(object):
    def __init__(self, name):
        self.name = name

    def setup(self):
        os.chdir(config.get_directory(self.name))
        for command in config.get_setup_commands(self.name):
            execute(command)

    def start(self, start_attached=False):
        os.chdir(config.get_directory(self.name))

        opts = '-d -s'
        if start_attached:
            opts = '-s'

        execute('tmux new-session {} {} {}'.format(opts, self.name, config.get_start_command(self.name)))

    def stop(self):
        execute('tmux send-keys -t {} C-c'.format(self.name))

    def attach(self):
        execute('tmux attach -t {}'.format(self.name))
