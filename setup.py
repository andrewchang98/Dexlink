from setuptools import setup, find_packages

setup(
    name='Dexlink',
    version='0.0.1',
    packages=find_packages(include=['dexutils', 'dexutils.*'])
)
