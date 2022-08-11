Release Notes
=============

.. towncrier release notes start

HexBytes v0.2.3 (2022-08-11)
----------------------------

Features
~~~~~~~~

- Type signature now accepts `memoryview` when creating HexBytes. It converts to a `bytes` internally,
  so not any performance benefit. But at least it's *possible* now, and mypy stops complaining. (`#22 <https://github.com/ethereum/hexbytes/issues/22>`__)


Performance improvements
~~~~~~~~~~~~~~~~~~~~~~~~

- Improve speed of the check for 0x at the beginning of the hex string. Similar to changes in
  eth-utils. (Technically merged by #22, but first posted in #21) (`#21 <https://github.com/ethereum/hexbytes/issues/21>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merged in latest changes from project template (`#24 <https://github.com/ethereum/hexbytes/issues/24>`__)


Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- `#25 <https://github.com/ethereum/hexbytes/issues/25>`__, `#26 <https://github.com/ethereum/hexbytes/issues/26>`__


HexBytes v0.2.2 (2021-08-25)
----------------------------

Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- Pass mypy tests with `--no-implicit-reexport` (`#15 <https://github.com/ethereum/hexbytes/pull/15>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge in template changes from the last year. Pass pydocstyle tests at the new major version. (`#16 <https://github.com/ethereum/hexbytes/issues/16>`__)


HexBytes v0.2.1 (2020-06-02)
----------------------------

Features
~~~~~~~~

- Officially support bytearray, int, and bool as inputs to :class:`~hexbytes.main.HexBytes`.
  Drop the dependency on eth-utils, for a much smaller & faster install. (`#12 <https://github.com/ethereum/hexbytes/issues/12>`__)


v0.2.0
--------------

Released June 3, 2019

- **Breaking Changes**

  - Dropped Python3.5 support (only in name at this release, but py3.6 features will be used soon
    `#10 <https://github.com/ethereum/hexbytes/pull/10>`_
- Features

  - A slice of HexBytes will now produce another HexBytes object
    `#9 <https://github.com/ethereum/hexbytes/pull/9>`_
- Maintenance

  - Added type hints
    `#7 <https://github.com/ethereum/hexbytes/pull/7>`_


v0.1.0
--------------

Released Mar 1, 2018

- Marked stable
- eth-utils v1.0.1 support

v0.1.0-beta.1
--------------

Released Feb 21, 2018

- pypy3 support
- eth-utils v1-beta.2 support
- Some generic template updates

v0.1.0-beta.0
--------------

Released Jan 30, 2018

- Tested a basic integration with eth-rlp
- Given the simplicity of the project and the longer usage history in web3.py,
  it is reasonable to bump to beta immediately.

v0.1.0-alpha.2
--------------

Released Jan 30, 2018

- Added hypothesis tests
- Added some docs
- Update eth-utils to get all required functionality
- Passes all tests

v0.1.0-alpha.1
--------------

- Launched repository, claimed names for pip, RTD, github, etc
