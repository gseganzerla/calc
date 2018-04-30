#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


package_name = 'calculadora'
filename = package_name + '.py'


setup(
    name=package_name,
    version=1.0,
    author='gui',
    author_email='gui.ironweasel',
    description='curl statistics made simple',
    url='https://github.com/reorx/httpstat',
    long_description="test teste teste",
    py_modules=[package_name],
    entry_points={
        'console_scripts': [
            'calculadora = calculadora:main'
        ]
    },
    license='License :: OSI Approved :: MIT License',
)