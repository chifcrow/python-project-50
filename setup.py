# python-project-50/setup.py

from setuptools import setup, find_packages

setup(
    name='gendiff',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gendiff = gendiff.gendiff:generate_diff',
        ],
    },
)
