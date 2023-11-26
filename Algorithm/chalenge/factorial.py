'''
compute a factorial of a number
'''

def factorial(val):

    # base case
    if val == 0:
        return 1
    elif val == 1:
        return 1
    else:
        res = val * factorial(val-1)

    return res

print('factorial computing: .....')
print(factorial(10))
