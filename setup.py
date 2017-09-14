from setuptools import setup

setup(
    name='Crawler',
    version='1.0',
    package_dir={' ': 'app'},
    install_requires=['pymysql', 'redis', 'elasticsearch']
)
