import actions
from decorators import command_line_wrapper


@command_line_wrapper
def attach(parser):
    parser.description = 'Attach a running app'
    parser.add_argument('app', help='The app to attach')
    args = parser.parse_args()

    actions.attach(args.app)


@command_line_wrapper
def start(parser):
    parser.description = 'Start an app'
    parser.add_argument('app', help='The app to start')
    parser.add_argument('-s', '--setup', action='store_true', default=False, dest='setup', help='Run setup commands before starting apps')
    parser.add_argument('-a', '--attach', action='store_true', default=False, dest='attach', help='Start the app in attached mode')
    args = parser.parse_args()

    actions.start(args.app, setup=args.setup, attach=args.attach)


@command_line_wrapper
def stop(parser):
    parser.description = 'Stop a running app'
    parser.add_argument('app', help='The app to stop')
    args = parser.parse_args()

    actions.stop(args.app)


@command_line_wrapper
def restart(parser):
    parser.description = 'Restart a running app'
    parser.add_argument('app', help='The app to restart')
    parser.add_argument('-s', '--setup', action='store_true', default=False, dest='setup', help='Run setup commands before starting')
    parser.add_argument('-a', '--attach', action='store_true', default=False, dest='attach', help='Start the app in attached mode')
    args = parser.parse_args()

    actions.restart(args.app, setup=args.setup, attach=args.attach)


@command_line_wrapper
def show(parser):
    parser.description = 'List configured apps'
    parser.add_argument('-a', '--alive', action='store_true', default=False, dest='alive', help='Only show running apps')
    args = parser.parse_args()

    actions.show(running_only=args.alive)
