import pytest

from fizz_buzz import fizz_buzz

# Can call FizzBuzz (Red)
def test_can_call_FizzBuzz():
    fizz_buzz(1)

# Get "1" when I pass in 1
def test_returns1when1passed():
    retval = fizz_buzz(1)
    assert retval=="1"

# Get "2" when I pass in 2
def test_returns1when1passed():
    retval = fizz_buzz(2)
    assert retval=="2"

