import yaml
from os.path import expanduser, join

from app import App


class Config(object):
    CONFIG_FILE = '.app_manager.yml'

    def __init__(self):
        with open(join(expanduser('~'), self.CONFIG_FILE), 'r') as fd:
            self.config = yaml.load(fd.read())

    def apps(self):
        for app_name in self.config.keys():
            yield self.app(app_name)

    def app(self, name):
        app_config = self.config.get(name)

        if app_config is None:
            raise Exception('This app has not been configured')

        return App(name, app_config.get('root'), app_config.get('start'), app_config.get('setup'))


config = Config()
