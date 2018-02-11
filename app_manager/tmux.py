import os
from subprocess import check_output, CalledProcessError


def tmux_exec(command):
    with open(os.devnull, 'w') as dev_null_fd:
        return check_output('tmux {command}'.format(command=command), shell=True, stderr=dev_null_fd)


def list():
    """
    @return [list<str>] list of running tmux session names
    """
    cmd_output = None

    try:
        cmd_output = tmux_exec('ls')
    except CalledProcessError:
        return []

    sessions = cmd_output.strip().split('\n')
    sessions = map(lambda session: session.split(':')[0], sessions)

    return sessions


def new_session(name, command, attached=False):
    options = '-s'

    if not attached:
        options = '-d ' + options

    tmux_exec('new-session {options} {name} {command}'.format(options=options, name=name, command=command))


def send_keys(session, keys):
    tmux_exec('send-keys -t {session} {keys}'.format(session=session, keys=keys))


def attach(session):
    tmux_exec('attach -t {session}'.format(session=session))
