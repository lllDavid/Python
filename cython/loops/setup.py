from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cyt_func.pyx")
)


# python setup.py build_ext --inplace
