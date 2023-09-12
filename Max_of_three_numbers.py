# Write a Python function to find the maximum of three numbers.


def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

x= input( 'x =')
y= input('y =')
z= input('z =')
max_number = max_of_three(x, y, z)
print(f"The maximum number is {max_number}")