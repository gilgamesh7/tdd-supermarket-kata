
def fizz_buzz( value ):
    ret_val = str(value)

    if value%3 == 0:
        ret_val = "Fizz"
    
    if value%5 == 0:
        ret_val = "Buzz"
    
    if value%3 == 0 and value%5 == 0:
        ret_val = "FizzBuzz"
    
    return ret_val