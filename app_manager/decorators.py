from argparse import ArgumentParser
from subprocess import CalledProcessError


def command_line_wrapper(func):
    def wrapper(*args, **kwargs):
        parser = ArgumentParser()
        parser.add_argument('-v', '--verbose', action='store_true', help='Show error stack traces')

        args = list(args)
        args.insert(0, parser)
        try:
            func(*args, **kwargs)

        # Catch errors from subprocesses failing.
        except CalledProcessError as e:
            if parser.parse_args().verbose is True:
                raise

            print('Command `{cmd}` exited with status {status}'.format(cmd=e.cmd, status=e.returncode))
            exit(e.returncode)

        except Exception as e:
            if parser.parse_args().verbose is True:
                raise

            print(e.message)

        except KeyboardInterrupt:
            if parser.parse_args().verbose is True:
                raise

            print('Received keyboard interrupt')

    return wrapper
