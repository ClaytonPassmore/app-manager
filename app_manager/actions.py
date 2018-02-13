import os
from time import sleep

from config import config
from utils import execute


def attach(app_name):
    manager = config.manager()

    if app_name not in manager.list():
        raise Exception('This app is not running')

    manager.attach(app_name)


def start(app_name, setup=False, attach=False):
    app = config.app(app_name)

    os.chdir(app.root)

    if setup:
        for command in app.setup_commands:
            execute(command)

    manager = config.manager()
    manager.new_session(app.name, app.start_command, attached=attach)


def stop(app_name):
    manager = config.manager()

    if app_name not in manager.list():
        raise Exception('This app is not running')

    keys = "$'\cc'" if config.mgr == 'screen' else 'C-c'
    manager.send_keys(app_name, keys)


def show(running_only=False):
    manager = config.manager()
    app_names = manager.list() if running_only else map(lambda app: app.name, config.apps())

    for app_name in sorted(app_names):
        print('-> {app}'.format(app=app_name))


def restart(app_name, setup=False, attach=False):
    stop(app_name)
    sleep(1)
    start(app_name, setup=setup, attach=attach)
