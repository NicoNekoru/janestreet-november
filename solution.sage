import math
var('x y')

def overlap_func(x, y):
    r1_squared = x**2 + y**2
    r2_squared = (x - 1)**2 + y**2
    term1 = r1_squared * math.asin(y / math.sqrt(r1_squared))
    term2 = r2_squared * math.asin(y / math.sqrt(r2_squared))
    return 8 * (term1 + term2 - y)

def inner_integral(x):
    return numerical_integral(lambda y: overlap_func(x, y), 0, x)[0]

result = numerical_integral(inner_integral, 0, 0.5)
print(result)
print((pi/6 - result[0]).n(100))