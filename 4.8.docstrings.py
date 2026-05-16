def sum(a,b):
    '''genrate docstring'''      #if you write multiline comment after starting a function and use __doc__ will print that as docstring
    return a+b
print(sum(4,6))
print(sum.__doc__)   # here (sum.__doc__) prints the comment as a docstring