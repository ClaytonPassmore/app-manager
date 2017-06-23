from setuptools import setup

setup(
    name='app-manager',
    version='0.1',
    description='Manage arbitrary apps',
    packages=['app_manager'],
    entry_points={
        'console_scripts': [
            'start=app_manager.commands:start',
            'stop=app_manager.commands:stop',
            'restart=app_manager.commands:restart',
            'attach=app_manager.commands:attach',
            'show=app_manager.commands:show'
        ]
    },
    install_requires=['pyyaml']
)
