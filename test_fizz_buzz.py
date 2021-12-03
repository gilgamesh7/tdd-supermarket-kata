import pytest

from fizz_buzz import fizz_buzz

# Can call FizzBuzz (Red)
def test_can_call_FizzBuzz():
    fizz_buzz(1)

# REFACTORED
# # Get "1" when I pass in 1
# def test_returns1when1passed():
#     retval = fizz_buzz(1)
#     assert retval=="1"

# # Get "2" when I pass in 2
# def test_returns1when1passed():
#     retval = fizz_buzz(2)
#     assert retval=="2"
def check_fizzbuzz( value, expected_value ):
    ret_val = fizz_buzz(value)
    assert ret_val == expected_value

# Get "1" when I pass in 1
def test_returns1when1passed():
    check_fizzbuzz(1,"1")

# Get "2" when I pass in 2
def test_returns1when1passed():
    check_fizzbuzz(2,"2")

# Get "Fizz" when I pass in 3
def test_returns_fizz_when3passed():
    check_fizzbuzz(3,"Fizz")

# Get "Buzz" when I pass in 5
def test_returns_buzz_when5passed():
    check_fizzbuzz(5, "Buzz")

# Get "Fizz" when I pass in multiple of 3
def test_returns_fizz_when_multiple3passed():
    check_fizzbuzz(6,"Fizz")  
    check_fizzbuzz(12,"Fizz")  
    check_fizzbuzz(18,"Fizz")  

# Get "Buzz" when I pass in multiple of 5
def test_returns_buzz_when_multiple5passed():
    check_fizzbuzz(10,"Buzz")  

def test_returns_fizzbuzz_when_multiple3and5passed():
    check_fizzbuzz(15,"FizzBuzz")