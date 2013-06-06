#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in oscar.__init__.py
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages
import os
import sys


PROJECT_DIR = os.path.dirname(__file__)

# Change to the current directory to solve an issue installing Oscar on the
# Vagrant machine.
if PROJECT_DIR:
    os.chdir(PROJECT_DIR)

setup(name='isells-theme-sale',
      version='1',
      url='https://github.com/alexzaporozhets/isells-theme-sale/',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="A domain-driven e-commerce framework for Django",
      long_description='qq',
      keywords="E-commerce, Django, domain-driven",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["sandbox*", "tests*"]),
      include_package_data=True,
      install_requires=[],
      dependency_links=[],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[]
      )
