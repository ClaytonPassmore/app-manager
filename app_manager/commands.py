import os
from argparse import ArgumentParser
from time import sleep

from project import Project
from config import config


def attach():
    parser = ArgumentParser(description='Attach a running app')
    parser.add_argument('project', help='The app to attach')
    args = parser.parse_args()

    if not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    try:
        Project(args.project).attach()
    except:
        print('Could not attach {}. Was it running?'.format(args.project))
        return


def start():
    parser = ArgumentParser(description='Start an app')
    parser.add_argument('project', help='The app to start')
    args = parser.parse_args()

    project_list = [args.project]

    if args.project == 'all':
        project_list = config.get_all_projects()
    elif not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    for project in project_list:
        Project(project).start()


def stop():
    parser = ArgumentParser(description='Stop a running app')
    parser.add_argument('project', help='The app to stop')
    args = parser.parse_args()

    project_list = [args.project]

    if args.project == 'all':
        project_list = config.get_all_projects()
    elif not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    for project in project_list:
        try:
            Project(project).stop()
        except:
            print('Could not stop {}. Was it running?'.format(project))
            return


def restart():
    parser = ArgumentParser(description='Restart a running app')
    parser.add_argument('project', help='The app to restart')
    args = parser.parse_args()

    project_list = [args.project]

    if args.project == 'all':
        project_list = config.get_all_projects()
    elif not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    for project in project_list:
        proj = Project(project)

        try:
            proj.stop()
        except:
            print('Could not stop {}. Was it running?'.format(project))

        sleep(1)
        proj.start()
