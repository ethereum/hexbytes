#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
        "hypothesis>=3.44.24,<=6.31.6",
        "eth-utils>=1.0.1,<3",
    ],
    "lint": [
        "flake8==6.0.0",
        "flake8-bugbear==23.3.23",
        "isort>=5.10.1",
        "mypy==0.971",
        "pydocstyle>=5.0.0",
        "black>=22",
    ],
    "doc": [
        "sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion>=0.5.3",
        "build>=0.9.0",
        "pytest-watch>=4.1.0",
        "tox>=4.0.0",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="hexbytes",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.3.1",
    description="""hexbytes: Python `bytes` subclass that decodes hex, with a readable console output""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/hexbytes",
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7, <4",
    extras_require=extras_require,
    py_modules=["hexbytes"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"hexbytes": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
