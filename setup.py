from setuptools import setup

setup(
    name = 'taskcli',
    version = '0.1.0',
    packages = ['taskcli'],
    entry_points = {
        'console_scripts': [
            'taskcli = taskcli.__main__:main'
        ]
    }
)
