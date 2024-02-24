def test_import_and_version():
    import hexbytes

    assert isinstance(hexbytes.__version__, str)
