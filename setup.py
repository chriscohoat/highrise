from distutils.core import setup

setup(
    name='highrisewrapper',
    version='0.1.0',
    author='Chris Cohoat',
    author_email='chris.cohoat@gmail.com',
    packages=['highrisewrapper', 'highrisewrapper.test'],
    url='https://github.com/chriscohoat/highrisewrapper',
    license='LICENSE.txt',
    description='Pythonic wrapper for Highrise.',
    long_description=open('README.txt').read(),
)
