from setuptools import setup

setup(
    name='dexlink'
    version='',
    description='Tools to link to Dexcom',
    long_description='',
    long_description_content_type='text/markdown',
    author='aChang',
    author_email='andrewchang99@gmail.com',
    url='https://github.com/andrewchang98/Dexlink.git',
    keywords='',
    packages=[
        'dexutils',
    ],
    install_requires=None,
    tests_require=None,
    setup_requires=['pydexcom'])
