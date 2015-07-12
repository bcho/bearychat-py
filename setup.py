# coding: utf-8

from setuptools import setup, find_packages


install_requires = [
    'requests'
]


setup(
    name='bearychat-py',
    version='0.1.1',
    author='hbc',
    author_email='bcxxxxxx@gmail.com',
    url='https://github.com/bcho/bearychat-py',
    description='A simple package for interacting with bearychat.',
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages('.'),
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
