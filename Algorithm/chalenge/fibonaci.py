def fibonacci(val):
    '''computing a fibonacci value'''

    # base case:
    if val == 0:
        return 0
    if val == 1:
        return 1
    else:
        # recursive function
        res = fibonacci(val-2) + fibonacci(val-1)

        return res

print('fibonaci sequence computing:')
print(fibonacci(10))