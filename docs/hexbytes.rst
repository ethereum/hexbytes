hexbytes package
================

Quickstart
------------

Install with:

.. code-block:: bash

    pip install hexbytes

Example :class:`~hexbytes.main.HexBytes` usage:

::

    >>> from hexbytes import HexBytes

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

HexBytes
---------------------

.. automodule:: hexbytes.main
    :members:
    :undoc-members:
    :show-inheritance:
