from setuptools import setup, find_packages

setup(
    name='randstr',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Small Python package for generating strings with random characters built on top of the random module.',
    long_description=open('README.md').read(),
    # install_requires=[''],
    url='https://github.com/CodeConfidant/randstr-random',
    author='Drew Hainer',
    author_email='codeconfidant@gmail.com'
)