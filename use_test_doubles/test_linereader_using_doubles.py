from unittest.mock import MagicMock
import pytest
from pytest import raises

from line_reader import read_from_file

@pytest.mark.skip
def test_CanReadFromFile():
    read_from_file("test_file")

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")

    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)

    return mock_open

def test_returnsCorrectString(mock_open, monkeypatch):

    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    result = read_from_file("test_file")

    mock_open.assert_called_once_with("test_file", "r")

    assert result == "test line"

def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)

    monkeypatch.setattr("os.path.exists", mock_exists)

    with raises(Exception):
        result = read_from_file("test_file")