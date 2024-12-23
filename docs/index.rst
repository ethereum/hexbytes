HexBytes
========

HexBytes is a *very* thin wrapper around the python built-in ``bytes`` class.

It adds these features:

#. Accepts more types for initializing values:

   * ``bool``
   * ``bytearray``
   * ``bytes``
   * ``int`` (non-negative)
   * ``str``
   * ``memoryview``
#. The representation at console (``__repr__``) is 0x-prefixed
#. ``to_0x_hex`` returns a 0x-prefixed hex string


Installation
------------

.. code-block:: bash

    python -m pip install hexbytes


.. toctree::
   :maxdepth: 1
   :caption: General

   Usage<hexbytes>
   release_notes

.. toctree::
   :maxdepth: 1
   :caption: Community

   contributing
   code_of_conduct
