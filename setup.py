# -*- coding:utf-8 -*-
from setuptools import setup

from astrid import __version__


setup(
    name="astrid",
    version=__version__,
    packages=["astrid"],
    install_requires=["aiohttp>=0.17.0"],
    author="Ayun Park",
    author_email="iamparkayun@gmail.com",
    description="A simple web framework based on aiohttp.",
    long_description="A simple web framework based on aiohttp.",
    url="http://github.com/Parkayun/astrid",
)
