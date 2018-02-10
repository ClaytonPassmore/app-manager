import os
from time import sleep

from config import config
from decorators import command_line_wrapper
from project import Project
from utils import execute


@command_line_wrapper
def attach(parser):
    parser.description = 'Attach a running app'
    parser.add_argument('project', help='The app to attach')
    args = parser.parse_args()

    if not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    try:
        Project(args.project).attach()
    except:
        print('Could not attach {}. Was it running?'.format(args.project))
        return


@command_line_wrapper
def start(parser):
    parser.description = 'Start an app'
    parser.add_argument('project', help='The app to start')
    parser.add_argument('-s', '--setup', action='store_true', default=False, dest='setup',
                        help='Run setup commands before starting apps')
    parser.add_argument('-a', '--attach', action='store_true', default=False, dest='attach',
                        help='Start the app in attached mode')
    args = parser.parse_args()


    start_attached = args.attach and args.project != 'all'
    project_list = [args.project]

    if args.project == 'all':
        project_list = config.get_all_projects()
    elif not config.project_exists(args.project):
        print('This app has not been configured. Check your {}'.format(config.CONFIG_FILE))

    for project in project_list:
        proj = Project(project)
        if args.setup:
            proj.setup()
        proj.start(start_attached=start_attached)


@command_line_wrapper
def stop(parser):
    parser.description = 'Stop a running app'
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
        sleep(0.2)


@command_line_wrapper
def restart(parser):
    parser.description = 'Restart a running app'
    parser.add_argument('project', help='The app to restart')
    parser.add_argument('-s', '--setup', action='store_true', default=False, dest='setup',
                        help='Run setup commands before starting apps')
    parser.add_argument('-a', '--attach', action='store_true', default=False, dest='attach',
                        help='Start the app in attached mode')
    args = parser.parse_args()

    start_attached = args.attach and args.project != 'all'
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
        if args.setup:
            proj.setup()
        proj.start(start_attached=start_attached)


@command_line_wrapper
def show(parser):
    parser.description = 'Show details about an app'
    parser.add_argument('filter', help='The filter to apply (e.g. all, alive)')
    args = parser.parse_args()

    if args.filter == 'alive':
        try:
            execute('tmux ls')
        except:
            pass
    elif args.filter == 'all':
        for project in sorted(config.get_all_projects()):
            print(project)
