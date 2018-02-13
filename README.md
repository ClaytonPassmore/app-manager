# App Manager
Manage your apps with the help of tmux (or screen)!

## Install
Run the following:
```bash
# Install pre-reqs (note that you can use screen instead of tmux)
brew install python && brew install tmux

# Clone the repo
git clone git@github.com:ClaytonPassmore/app-manager.git

# Install the package
pip install -e ./app-manager
```

## Configure
Create the following file: `~/.app_manager.yml`.

Fill it with the apps you want to run in the following format:
```yml
<project name>:
  root: <directory of app>
  start: <command to execute to start the app>
  setup:
    - <list of commands to execute before startup>
    - <e.g. npm install>
    - <e.g. bundle install>
<second project>:
  ...
```

You can also specify the window manager you would like to use with the `manager` key.
Tmux is used by default, but screen is also available.
```yml
manager: screen
...
```


## Commands
Installing this package gives you the following commands:

### `start`
```
usage: start [-h] [-v] [-s] [-a] app

Start an app

positional arguments:
  app            The app to start

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Show error stack traces
  -s, --setup    Run setup commands before starting
  -a, --attach   Start the app in attached mode
```


### `attach`
```
usage: attach [-h] [-v] app

Attach a running app

positional arguments:
  app            The app to attach

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Show error stack traces
```


### `restart`
```
usage: restart [-h] [-v] [-s] [-a] app

Restart a running app

positional arguments:
  app            The app to restart

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Show error stack traces
  -s, --setup    Run setup commands before starting
  -a, --attach   Start the app in attached mode
```


### `show`
```
usage: show [-h] [-v] [-a]

List configured apps

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Show error stack traces
  -a, --alive    Only show running apps
```
