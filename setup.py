#!/usr/bin/env python

from distutils.core import setup

setup(name='OrgProbe',
      version='2.1.2',
      description='Blocked.org.uk probe software',
      author='Open Rights Group',
      author_email='blocked@openrightsgroup.org',
      url='https://github.com/openrightsgroup/OrgProbe',
      packages=['OrgProbe'],
      scripts=['orgprobe'],
      requires=[
          'pika(>=0.10.0)',
          'requests(==2.12.0)',
          'configparser(==3.5.0)'
      ]
      )
