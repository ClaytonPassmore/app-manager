import os
from re import match
from subprocess import check_output, CalledProcessError


def screen_exec(command):
    with open(os.devnull, 'w') as dev_null_fd:
        return check_output('screen {command}'.format(command=command), shell=True, stderr=dev_null_fd)


def list():
    """
    @return [list<str>] list of running screen session names
    """
    session_regex = r"\s\d+\.(?P<session>\w+).*"
    cmd_output = None

    try:
        cmd_output = screen_exec('-list')

    # Screen's list command always exits with a non-zero status code so we have
    # to salvage the output from the exception.
    except CalledProcessError as e:
        cmd_output = e.output

    sessions = cmd_output.strip().split('\n')
    sessions = sessions[1:-1]
    sessions = map(lambda session: match(session_regex, session).group('session'), sessions)

    return sessions


def new_session(name, command, attached=False):
    options = '-S'

    if not attached:
        options = options + 'dm'

    screen_exec('{options} {name} {command}'.format(options=options, name=name, command=command))


def send_keys(session, keys):
    screen_exec('-S {session} -p 0 -X stuff {keys}'.format(session=session, keys=keys))


def attach(session):
    screen_exec('-r {session}'.format(session=session))
