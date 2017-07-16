from setuptools import setup, Extension

setup(name="cpyext-benchmarks",
      ext_modules = [Extension('simple', ['simple.c'])])
