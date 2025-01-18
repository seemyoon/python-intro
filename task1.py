# create any func and use inside of it a return statement
# ensure that return is a statement, not an expression
def my_func(a):
    return a


my_func(4)
def my_func2(b):
    if b >= 3:
        return 'your number 3 or more than 3'
    else:
        return 'your number less than 3'

my_func2(4)