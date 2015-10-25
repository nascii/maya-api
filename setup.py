#!/usr/bin/env python
from distutils.core import setup

package_name = 'iddybiddy'
package_data = {}
package_data[package_name] = ['VERSION']
__version__ = open(package_name + '/VERSION', 'r').read()

setup(
    name=package_name,
    version=__version__,
    description='',
    author='Corpix',
    author_email='me@corpix.ru',
    url='',
    packages=[
        package_name
    ],
    package_data=package_data
)
