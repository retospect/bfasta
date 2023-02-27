from bfasta import FastAreader
import os


def test_commandline_installed():
    reader = FastAreader("tests/test.fa")
    for header, seq in reader.readFasta():
        assert (
            "pyroOgun20001 CP003316 Pyrobaculum oguniense TE7, complete genome."
            == header
        )
        assert "GAGA" in seq
        break
    header, seq = next(reader.readFasta())
    assert (
        "pyroOgun20001 CP003316 Pyrobaculum oguniense TE7, complete genome." == header
    )
    assert "GAGA" in seq
