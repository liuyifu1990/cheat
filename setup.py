from distutils.core import setup
import os

setup(
    name         = 'cheattest',
    version      = '1.0.0',
    author       = 'liuyifu1990',
    author_email = 'liuyifu1990@foxmail.com',
    license      = 'GPL3',
    description  = 'just my self-practice',
    packages     = [
        'cheatfunc',
    ],
    package_data = {
        '':["*.ini"],
    },
    scripts          = ['bin/cheat'],
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ]
)
