# App Manager
Manage your apps with the help of tmux!

## Install
Run the following:
```bash
# Install pre-reqs
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


## Commands
Installing this package gives you the following commands:

### `start`
```
usage: start [-h] [-s] [-a] project

Start an app

positional arguments:
  project       The app to start

optional arguments:
  -h, --help    show this help message and exit
  -s, --setup   Run setup commands before starting apps
  -a, --attach  Start the app in attached mode
```


### `attach`
```
usage: attach [-h] project

Attach a running app

positional arguments:
  project     The app to attach

optional arguments:
  -h, --help  show this help message and exit
```


### `restart`
```
usage: restart [-h] [-s] [-a] project

Restart a running app

positional arguments:
  project       The app to restart

optional arguments:
  -h, --help    show this help message and exit
  -s, --setup   Run setup commands before starting apps
  -a, --attach  Start the app in attached mode
```


### `show`
```
usage: show [-h] filter

Show details about an app

positional arguments:
  filter      The filter to apply (e.g. "alive")

optional arguments:
  -h, --help  show this help message and exit
```
