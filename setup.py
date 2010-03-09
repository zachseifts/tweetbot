#!/usr/bin/env python

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.1'

def read(fname):
    ''' Utility function to read the README.markdown file.'''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author='Zach Seifts',
    author_email='zach.seifts+tweetbot@gmail.com',
    install_requires = ['setuptools', 'python-twitter'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
    ],
    description=('A python powered twitter library.'),
    long_description=read('README.markdown'),
    license='BSD',
    keywords='twitter bots',
    name='tweetbot',
    version=__version__,
    packages = ['tweetbot'],
)
