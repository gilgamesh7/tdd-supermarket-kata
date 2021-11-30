
def fizz_buzz( value ):
    ret_val = str(value)

    if value%3 == 0:
        ret_val = "Fizz"
    
    if value%5 == 0:
        ret_val = "Buzz"
    
    return ret_val