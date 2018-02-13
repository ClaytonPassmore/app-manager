import yaml
from os.path import expanduser, join

import screen
import tmux
from app import App


class Config(object):
    CONFIG_FILE = '.app_manager.yml'
    MANAGER_KEY = 'manager'

    MANAGERS = {
        'tmux': tmux,
        'screen': screen
    }

    def __init__(self):
        self.mgr = 'tmux'

        with open(join(expanduser('~'), self.CONFIG_FILE), 'r') as fd:
            self.config = yaml.load(fd.read())

        # Check for an alternative window manager.
        if self.MANAGER_KEY in self.config.keys():
            self.mgr = self.config[self.MANAGER_KEY]
            del self.config[self.MANAGER_KEY]

    def apps(self):
        for app_name in self.config.keys():
            yield self.app(app_name)

    def app(self, name):
        app_config = self.config.get(name)

        if app_config is None:
            raise Exception('This app has not been configured')

        return App(name, app_config.get('root'), app_config.get('start'), app_config.get('setup'))

    def manager(self):
        return self.MANAGERS[self.mgr]

config = Config()
