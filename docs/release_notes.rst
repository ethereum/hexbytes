Release Notes
=============

.. towncrier release notes start

hexbytes v1.3.1 (2025-05-14)
----------------------------

Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- `#53 <https://github.com/ethereum/hexbytes/issues/53>`__


Performance Improvements
~~~~~~~~~~~~~~~~~~~~~~~~

- Add an optimized ``__reduce__`` method to the ``HexBytes`` class that avoids validation when pickling / unpickling since the instance is already validated on creation. (`#52 <https://github.com/ethereum/hexbytes/issues/52>`__)


hexbytes v1.3.0 (2025-01-13)
----------------------------

Features
~~~~~~~~

- Merge template, adding `py313` suppport and removing ``bumpversion`` for ``bump-my-version`` (`#50 <https://github.com/ethereum/hexbytes/issues/50>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Bump ``towncrier`` dep from ``>=21,<22`` to ``>=24,<25`` (`#49 <https://github.com/ethereum/hexbytes/issues/49>`__)


hexbytes v1.2.1 (2024-06-17)
----------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Update docs structure, adding Contribution and Code of Conduct sections (`#44 <https://github.com/ethereum/hexbytes/issues/44>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Drop ``bumpversion`` for ``bump-my-version`` and add ``make package-test`` to build and test the package before pushing to pypi. (`#44 <https://github.com/ethereum/hexbytes/issues/44>`__)
- Run ``mypy`` with local deps installed instead of ``pre-commit`` ``mirrors-mypy`` hook. (`#47 <https://github.com/ethereum/hexbytes/issues/47>`__)


Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- `#46 <https://github.com/ethereum/hexbytes/issues/46>`__


hexbytes v1.2.0 (2024-03-19)
----------------------------

Features
~~~~~~~~

- Add ``to_0x_hex()`` method to provide a quick, explicit way to get an 0x-prefixed string (`#43 <https://github.com/ethereum/hexbytes/issues/43>`__)


hexbytes v1.1.0 (2024-03-01)
----------------------------

Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Change the name of ``master`` branch to ``main`` (`#40 <https://github.com/ethereum/hexbytes/issues/40>`__)
- Merge template updates, notably adding py312 support (`#41 <https://github.com/ethereum/hexbytes/issues/41>`__)


hexbytes v1.0.0 (2023-11-07)
----------------------------

Breaking Changes
~~~~~~~~~~~~~~~~

- Move HexBytes prepend of ``0x`` from ``hex`` method to ``__repr__`` to not break ``hex`` of parent ``bytes`` class (`#38 <https://github.com/ethereum/hexbytes/issues/38>`__)
- Drop python 3.7 support (`#39 <https://github.com/ethereum/hexbytes/issues/39>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added missing `build` dependency. (`#32 <https://github.com/ethereum/hexbytes/issues/32>`__)
- Add ``build.os`` config for readthedocs (`#34 <https://github.com/ethereum/hexbytes/issues/34>`__)
- Change to using ``pre-commit`` to manage linting tools (`#35 <https://github.com/ethereum/hexbytes/issues/35>`__)
- Merge project template updates and bump mypy to v1.5.1 (`#36 <https://github.com/ethereum/hexbytes/issues/36>`__)
- Merge template - .gitignore updates and other fixes (`#37 <https://github.com/ethereum/hexbytes/issues/37>`__)
- Merge template updates, including additional linting, move most lint config to pyproject.toml (`#39 <https://github.com/ethereum/hexbytes/issues/39>`__)


HexBytes v0.3.1 (2023-06-08)
----------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- pull in ethereum-python-project-template updates (`#31 <https://github.com/ethereum/hexbytes/issues/31>`__)


Internal Changes - for hexbytes Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- pull in ethereum-python-project-template updates (`#31 <https://github.com/ethereum/hexbytes/issues/31>`__)


HexBytes v0.3.0 (2022-08-17)
----------------------------

Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- `#28 <https://github.com/ethereum/hexbytes/issues/28>`__


Breaking changes
~~~~~~~~~~~~~~~~

- Drop support for Python 3.6, update Sphinx doc dependency requirement (`#27 <https://github.com/ethereum/hexbytes/issues/27>`__)


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
