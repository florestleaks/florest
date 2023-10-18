"""Test florest."""

import florest


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(florest.__name__, str)
