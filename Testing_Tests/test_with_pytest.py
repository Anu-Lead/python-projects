from .with_pytest import add
import pytest


@pytest.fixture()
def fixture_for_test():
    return 10


@pytest.mark.numbers
def test_add(db):
    assert add(5, db) == 10
    assert add(5, 5) == 10
    assert 3 in (5, 1, 3, 7, 5)


@pytest.mark.strings
def test_add_with_strings():
    assert add("hello", "world") == "hello world"


@pytest.mark.skip(reason="Not Ready Yet")
def test_add_with_st():
    assert add("hello", "world") == "hello world"
