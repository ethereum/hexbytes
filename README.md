# HexBytes

[![Join the conversation on Discord](https://img.shields.io/discord/809793915578089484?color=blue&label=chat&logo=discord&logoColor=white)](https://discord.gg/GHryRvPB84)
[![Build Status](https://circleci.com/gh/ethereum/hexbytes.svg?style=shield)](https://circleci.com/gh/ethereum/hexbytes)
[![PyPI version](https://badge.fury.io/py/hexbytes.svg)](https://badge.fury.io/py/hexbytes)
[![Python versions](https://img.shields.io/pypi/pyversions/hexbytes.svg)](https://pypi.python.org/pypi/hexbytes)
[![Docs build](https://readthedocs.org/projects/hexbytes/badge/?version=latest)](https://hexbytes.readthedocs.io/en/latest/?badge=latest)

Python `bytes` subclass that decodes hex, with a readable console output

Read the [documentation](https://hexbytes.readthedocs.io/).

View the [change log](https://hexbytes.readthedocs.io/en/latest/release_notes.html).

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
