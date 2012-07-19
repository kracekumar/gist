#! /usr/bin/env python
#! -*- coding: utf-8 *-*-

import sys
from setuptools import Command, setup, find_packages

readme = open('README.rst', 'r').read()
setup(
    name='gist',
    version='0.0.2',
    url='https://github.com/kracekumar/gist',
    license='BSD',
    author='kracekumar',
    author_email='me@kracekumar',
    description='Command Line Interface for pasting to gist.github.com',
    long_description=readme,
    packages=find_packages(),
    install_requires=['requests', 'argparse'],
    entry_points={
        'console_scripts': [
            'gist = gist.commands:main',
            ]
    },
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    )