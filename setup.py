# -*- coding:utf-8 -*-
import re
from setuptools import setup


with open('hayeonsoo/__init__.py') as f:
    version = re.search(r'__version__\s*=\s*\'(.+?)\'', f.read()).group(1)
assert version

setup(
    name="hayeonsoo",
    version=version,
    packages=["hayeonsoo", "hayeonsoo.middleware"],
    install_requires=["aiohttp>=0.17.0", "Jinja2>=2.8", "uvloop>=0.4.10"],
    tests_require=["pytest==2.8.3", "pytest-cov==2.2.0"],
    author="Ayun Park",
    author_email="iamparkayun@gmail.com",
    description="aiohttp for humans.",
    url="http://github.com/Parkayun/hayeonsoo",
)
