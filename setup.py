"""
MIT License

Copyright (c) 2024 Jordan Maxwell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup
import sys
import os

def get_version() -> str:
    """
    Get the package version from the environment variables.
    """

    major = os.environ.get('MAJOR', '1')
    minor = os.environ.get('MINOR', '0')
    patch = os.environ.get('PATCH', '0')

    return f'{major}.{minor}.{patch}'

def get_readme(file_path: str = 'README.md') -> str:
    """
    Returns the contents of the requested README file
    """

    with open(file_path, 'r') as f:
        return f.read()

def get_requirements(file_path: str = 'requirements.txt') -> list:
    """
    Returns the contents of the requested requirements.txt
    file
    """

    try: # for pip >= 10
        from pip._internal.req import parse_requirements
    except ImportError: # for pip <= 9.0.3
        from pip.req import parse_requirements

    install_reqs = parse_requirements(file_path, session='hack')
    reqs = [str(ir.requirement) for ir in install_reqs]
    
    return reqs

def get_package_url(main_module: str) -> str:
    """
    Returns the URL for the package
    """

    repository_name = main_module.replace('_', '-')
    return f'https://github.com/thetestgame/{repository_name}'

def main() -> int:
    """
    Main entry point for the setup script
    """

    # Define some constants
    module_name = 'panda3d_itchio'

    # Run the setup
    setup(
        name=module_name,
        description='',
        long_description=get_readme(),
        long_description_content_type='text/markdown',
        license='MIT',
        version=get_version(),
        author='Jordan Maxwell',
        maintainer='Jordan Maxwell',
        url=get_package_url(module_name),
        packages=[module_name],
        install_requires=get_requirements(),
        classifiers=[
            'Programming Language :: Python :: 3',
        ])
    
    return 0

# Run the main function
if __name__ == '__main__':
    sys.exit(main())