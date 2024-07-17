#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tap-exacttarget',
    version='1.7.1',
    description='Singer.io tap for extracting data from the ExactTarget API -- Updated to Salesforce-FuelSDK-Sans',
    author='Fishtown Analytics',
    url='http://fishtownanalytics.com',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_exacttarget'],
    install_requires=[
        'funcy==2.0.0',
        'singer-python==5.12.1',
        'python-dateutil==2.6.0',
        'voluptuous==0.13.1',
        'Salesforce-FuelSDK-Sans==1.3.1'
    ],
    extras_require={
        'test': [
            'pylint==2.10.2',
            'astroid==2.7.3',
            'nose'
        ],
        'dev': [
            'ipdb==0.11'
        ]
    },
    entry_points='''
    [console_scripts]
    tap-exacttarget=tap_exacttarget:main
    ''',
    packages=find_packages(),
    package_data={
        'tap_exacttarget': ['schemas/*.json']
    }
)
