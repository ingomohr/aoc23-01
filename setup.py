from setuptools import setup, find_packages

setup(
    name='aoc01',
    version='0.1.0',
    description='Solves puzzle #1 of AOC 2023',
    author='Ingo Mohr',
    author_email='tellastory73@gmail.com',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'numpy',
        'pandas'
        # Add other dependencies here
    ],
)
