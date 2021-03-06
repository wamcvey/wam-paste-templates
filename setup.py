from setuptools import setup, find_packages
import sys, os

version = '0.2.2'

setup(name='wam_paste_template',
      version=version,
      description="Boilerplate templates for WAM's development",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='William McVey',
      author_email='wam@wamber.net',
      url='http://www.wamber.net/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      package_data = {
      	'wam_paste_template':  ['*_templates/*'],
      },
      install_requires=[
          # -*- Extra requirements: -*-
	  "PasteScript",
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      wam_cli = wam_paste_template:CLI_Template
      """,
      )
