import os, codecs
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='numeralru',
    version='0.0.1',
    description="Package to convert numbers to russian words",
    long_description=codecs.open(os.path.join(here, 'README.rst'), 
                                 "r", "utf-8").read(),
    license="MIT",
    author='Maksim Misin',
    keywords=" number words russian case gender",
    url='https://github.com/MaksMshn/numeralru',
    test_suite='tests',
    packages=["numeralru"],
)
