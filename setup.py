from setuptools import setup, find_packages
import os
import re

def read_file(_file):
    current = os.path.abspath(os.path.dirname(__file__))
    _github_path = os.path.join(current, _file)
    with open(_github_path) as f:
        _data = f.read()
    return _data


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)


version = get_version('real_useragent')
setup(
    name='real_useragent',
    version=version,
    description='Get Real user agent from auto update',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/useragenter/real-useragent',
    author='Mohammadreza (MMDRZA)',
    author_email='Pymmdrza@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    keywords=['user-agent', 'useragenter', 'useragent', 'user agent', 'useragent', 'real user agent', 'real-useragent'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Bug Reports': 'https://github.com/useragenter/real-useragent/issues',
        'Source': 'https://github.com/useragenter/real-useragent',
    },
)
