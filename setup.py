from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='tweetbot',
      version=version,
      description="A python based twitter bot framework.",
      long_description="""\
""",
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
      keywords='twitter, bot',
      author='Zach Seifts',
      author_email='zach.seifts+tweetbot@gmail.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires = ['setuptools', 'python-twitter'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
