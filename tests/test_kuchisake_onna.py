import sys

import pytest


@pytest.mark.parametrize("answer", ["yes", "no"])
def test_import(answer, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: answer)

    sys.modules.pop("kuchisake_onna", None)

    with pytest.raises(Exception):
        import kuchisake_onna
