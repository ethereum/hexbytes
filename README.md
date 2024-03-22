# HexBytes

[![Join the conversation on Discord](https://img.shields.io/discord/809793915578089484?color=blue&label=chat&logo=discord&logoColor=white)](https://discord.gg/GHryRvPB84)
[![Build Status](https://circleci.com/gh/ethereum/hexbytes.svg?style=shield)](https://circleci.com/gh/ethereum/hexbytes)
[![PyPI version](https://badge.fury.io/py/hexbytes.svg)](https://badge.fury.io/py/hexbytes)
[![Python versions](https://img.shields.io/pypi/pyversions/hexbytes.svg)](https://pypi.python.org/pypi/hexbytes)
[![Docs build](https://readthedocs.org/projects/hexbytes/badge/?version=latest)](https://hexbytes.readthedocs.io/en/latest/?badge=latest)

Python `bytes` subclass that decodes hex, with a readable console output

Read more in the [documentation on ReadTheDocs](https://hexbytes.readthedocs.io/). [View the change log](https://hexbytes.readthedocs.io/en/latest/release_notes.html).

## Quickstart

```sh
python -m pip install hexbytes
```

```py
# convert from bytes to a prettier representation at the console
>>> HexBytes(b"\x03\x08wf\xbfh\xe7\x86q\xd1\xeaCj\xe0\x87\xdat\xa1'a\xda\xc0 \x01\x1a\x9e\xdd\xc4\x90\x0b\xf1;")
HexBytes('0x03087766bf68e78671d1ea436ae087da74a12761dac020011a9eddc4900bf13b')

# HexBytes accepts the hex string representation as well, ignoring case and 0x prefixes
>>> hb = HexBytes('03087766BF68E78671D1EA436AE087DA74A12761DAC020011A9EDDC4900BF13B')
HexBytes('0x03087766bf68e78671d1ea436ae087da74a12761dac020011a9eddc4900bf13b')

# get the first byte:
>>> hb[0]
3

# show how many bytes are in the value
>>> len(hb)
32

# cast back to the basic `bytes` type
>>> bytes(hb)
b"\x03\x08wf\xbfh\xe7\x86q\xd1\xeaCj\xe0\x87\xdat\xa1'a\xda\xc0 \x01\x1a\x9e\xdd\xc4\x90\x0b\xf1;"
```

## Contributing

If you would like to hack on hexbytes, please check out the [Snake Charmers
Tactical Manual](https://github.com/ethereum/snake-charmers-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Documentation

We use [pre-commit](https://pre-commit.com/) to maintain consistent code style. Once
installed, it will run automatically with every commit. You can also run it manually
with `make lint`. If you need to make a commit that skips the `pre-commit` checks, you
can do so with `git commit --no-verify`.

### Development Environment Setup

To get started, fork the repository to your own github account, then clone it to your
development machine:

```sh
git clone git@github.com:your-github-username/hexbytes.git
```

Next, install the development dependencies. We recommend using a virtual environment,
such as [`virtualenv`](https://virtualenv.pypa.io/en/stable/)

```sh
cd hexbytes
virtualenv -p python venv
. venv/bin/activate
python -m pip install -e ".[dev]"
pre-commit install
```

### Releasing a New Version

Cutting a new release has 3 steps which should be executed in this order:

1. Build and test the package
1. Compile the release notes
1. Build the final release and push to pypi and github

#### Build and Test the Package

```sh
make package-test
```

This will build the package and run some basic tests against it in a virtualenv.

#### Compile Release Notes

```sh
make notes bump=VERSION_PART_TO_BUMP
```

This will compile all the newsfragments and generate release notes for the version
you are releasing.

#### Build and Push New Version to pypi and github

```sh
make release bump=VERSION_PART_TO_BUMP
```

This command will:

- Bump the version number as specified.
- Create a git commit and tag for the new version.
- Build the package.
- Push the commit and tag to github.
- Push the new package files to pypi.

### About Bumping the Version

`VERSION_PART_TO_BUMP` must be one of: `major`, `minor`, `patch`, `stage`, or `devnum`.

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, specify which part to bump, like
`make notes bump=minor` or `make notes bump=devnum`. This is typically done from the
main branch, except when releasing a beta (in which case the beta is released from main,
and the previous stable branch is released from said branch).

If you are in a beta version, `make notes bump=stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the new version explicitly, like `make release bump="--new-version 4.0.0-alpha.1"`

You can see what the result of bumping any particular version part would be with
`bump-my-version show-bump`
