"""
A setuptools based tool, rgwcmd provides a cmd interface to the Rados Gateway Admin REST API calls.

See:
http://docs.ceph.com/docs/master/radosgw/adminops/
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'rgwcmd/README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rgwcmd',

    version='0.2',

    description='A commandline toll to make REST API calls to the Rados Gateway.',
    long_description=long_description,

    url='https://github.com/safiyat/rgwcmd',

    author='Cloud Platform Team, Snapdeal',
    author_email='cloudplatform@snapdeal.com',

    license='GPLv2',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers, System Administrators',
        'Topic :: System :: Software Distribution',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='radosgateway commandline tool',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'argparse>=1.2.1',
        'requests>=2.9.1',
        'requests-aws>=0.1.8'
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[],

    entry_points={
        'console_scripts': [
            'rgwcmd=rgwcmd:main',
        ],
    },
)
