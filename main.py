#WRITE YOUR CODE IN THIS FILE

def close10(x, y):
    if abs(10-x) < abs(10-y):
        return x
    elif abs(10-x) > abs(10-y):
        return y
    else:
        return 0

print(close10(5,2))
