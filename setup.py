from setuptools import setup
import os

setup(
    name='panda3d_itchio',
    description='A collection of helpful utility methods and constants for working with the Panda3D game engine',
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    version=os.environ.get('VERSION', '1.0.0'),
    author='Jordan Maxwell',
    maintainer='Jordan Maxwell',
    url='https://github.com/thetestgame/panda3d-itchio',
    packages=['panda3d_itchio'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'panda3d-rest==1.0.3'
    ])
