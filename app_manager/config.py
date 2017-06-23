import os
import yaml
from os.path import expanduser


class Config(object):
    CONFIG_FILE = '.app_manager.yml'

    def __init__(self):
        with open(os.path.join(expanduser('~'), self.CONFIG_FILE), 'r') as fd:
            self.config = yaml.load(fd.read())

    def project_exists(self, project):
        return project in self.config.keys()

    def get_setup_commands(self, project):
        return self.config[project]['setup']

    def get_start_command(self, project):
        return self.config[project]['start']

    def get_all_projects(self):
        return self.config.keys()

    def get_directory(self, project):
        return self.config[project]['root']


config = Config()
