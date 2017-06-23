# App Manager
Manage your apps with the help of screen!

## Install
Run the following:
```bash
# Install pre-reqs
brew install python && brew install screen

# Clone the repo
git clone $THIS_REPO

# Install the package
pip install -e ./app-manager
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


### `stop`
```
usage: stop [-h] project

Stop a running app

positional arguments:
  project     The app to stop

optional arguments:
  -h, --help  show this help message and exit
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
