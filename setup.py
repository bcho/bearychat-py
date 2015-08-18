# coding: utf-8

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


install_requires = [
    'requests'
]


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='bearychat-py',
    version='0.2.0',
    author='hbc',
    author_email='bcxxxxxx@gmail.com',
    url='https://github.com/bcho/bearychat-py',
    description='A simple package for interacting with bearychat.',
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages('.', exclude=['tests*']),
    zip_safe=False,
    install_requires=install_requires,

    cmdclass={'test': PyTest},
    tests_require=['pytest', 'responses'],

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
