#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.1'

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
    description='A twitter bot library.',
    license='BSD',
    keywords='twitter bots',
    name='tweetbot',
    version=__version__,
    packages = ['tweetbot'],
)
