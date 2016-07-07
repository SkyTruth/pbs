#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itertools as it

from setuptools import setup

try:
    from pypandoc import convert
    long_description = convert('README.md', 'rst')
except IOError:
    print("warning: README.md not found")
    long_description = ""
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    long_description = ""


install_requires = [
    'click',
    'pybossa-client>=1.0.4, <1.0.5',
    'requests',
    'nose',
    'mock',
    'coverage',
    'rednose',
    'simplejson',
    'jsonschema',
    'polib',
    'watchdog']


extras_require = {
    'docs': ['pypandoc']
}
extras_require['all'] = list(
    it.chain.from_iterable(extras_require.values())) + install_requires

setup(
    name="pybossa-pbs",
    version="2.0.3",
    author="SciFabric LTD",
    author_email="info@scifabric.com",
    description="PyBossa command line client",
    long_description=long_description,
    license="AGPLv3",
    url="https://github.com/PyBossa/pbs",
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',],
    py_modules=['pbs', 'helpers', 'pbsexceptions'],
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points='''
        [console_scripts]
        pbs=pbs:cli
    '''
)
