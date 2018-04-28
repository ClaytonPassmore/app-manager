import os
from time import sleep

from config import config
from colours import OK_GREEN, FAIL
from utils import execute, write, write_line


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


def stop(app_names):
    manager = config.manager()
    running_apps = manager.list()

    if len(app_names) == 0:
        app_names = running_apps

    for app_name in app_names:
        write('Stopping {app} ... '.format(app=app_name))
        if app_name not in running_apps:
            write_line('fail', colour=FAIL)
            continue

        keys = "$'\cc'" if config.mgr == 'screen' else 'C-c'
        manager.send_keys(app_name, keys)
        write_line('ok', colour=OK_GREEN)


def show(all=False):
    manager = config.manager()
    running_apps = manager.list()
    app_names = map(lambda app: app.name, config.apps()) if all else running_apps

    for app_name in sorted(app_names):
        mark = '=>' if app_name in running_apps else '->'
        print('{mark} {app}'.format(mark=mark, app=app_name))


def restart(app_name, setup=False, attach=False):
    stop(app_name)
    sleep(1)
    start(app_name, setup=setup, attach=attach)
