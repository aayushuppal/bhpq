"""Setup script for bhpq"""


import os.path
from typing import Dict

from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# read version
_version_info: Dict[str, str] = {}
with open(os.path.join(HERE, "bhpq/_version.py")) as fid:
    exec(fid.read(), _version_info)


# This call to setup() does all the work
setup(
    name="bhpq",
    version=_version_info["__version__"],
    description="Binary Heap Priority Queue",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aayushuppal/bhpq",
    author="Aayush Uppal",
    author_email="aayuppal@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["bhpq"],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)
