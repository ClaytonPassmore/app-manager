import os
from time import sleep

import tmux
from config import config
from utils import execute


def attach(app_name):
    if app_name not in tmux.list():
        raise Exception('This app is not running')

    tmux.attach(app_name)


def start(app_name, setup=False, attach=False):
    app = config.app(app_name)

    os.chdir(app.root)

    if setup:
        for command in app.setup_commands:
            execute(command)

    tmux.new_session(app.name, app.start_command, attached=attach)


def stop(app_name):
    if app_name not in tmux.list():
        raise Exception('This app is not running')

    tmux.send_keys(app_name, 'C-c')


def show(running_only=False):
    app_names = tmux.list() if running_only else map(lambda app: app.name, config.apps())

    for app_name in sorted(app_names):
        print('-> {app}'.format(app=app_name))


def restart(app_name, setup=False, attach=False):
    stop(app_name)
    sleep(1)
    start(app_name, setup=setup, attach=attach)
