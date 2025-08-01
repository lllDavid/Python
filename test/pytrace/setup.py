from setuptools import setup, Extension

module = Extension('mytrace', sources=['mytrace.c'])

setup(
    name='mytrace',
    version='1.0',
    ext_modules=[module],
)