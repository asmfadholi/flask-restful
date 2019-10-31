# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="dts-project",
    version="0.1.0",
    description="plat number detection",
    license="MIT",
    author="asmfadholi",
    packages=find_packages(),
    install_requires=['numpy>=1.9.1'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
