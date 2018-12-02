# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

# Version
with open(path.join(path.dirname(__file__), 'bookworm', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(
    name="bookworm",
    version=VERSION,
    url="https://github.com/prosegrinder/python-bookworm",

    author="David L. Day",
    author_email="dday376@gmail.com",

    description="A text analytics library for prose fiction.",
    long_description=LONG_DESCRIPTION,

    python_requires='>=3.4',
    packages=[
        'bookworm'
    ],
    package_dir={'bookworm': 'bookworm'},
    package_data={
        '': ['LICENSE', '*.rst', 'MANIFEST.in'],
    },
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
