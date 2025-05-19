from importlib.util import find_spec

import pytest


def test_pytest_is_working():
    """A dummy test to ensure pytest runs."""
    assert True


def test_import_package():
    """Test that the main package can be imported."""
    try:
        find_spec("your_package")  # replace with your real package name
    except ImportError:
        pytest.fail("Could not import 'your_package'")
