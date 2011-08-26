from distutils.core import setup

setup(
    name='highrise',
    version='0.1.0',
    author='Chris Cohoat',
    author_email='chris.cohoat@gmail.com',
    packages=['highrise', 'highrise.test'],
    url='https://github.com/chriscohoat/highrise',
    license='LICENSE.txt',
    description='Pythonic wrapper for Highrise.',
    long_description=open('README.md').read(),
)