import numpy as np
import math

# making the x points
def making_x_points(x1_domain, x2_domain):
    x = []
    
    for i in range(x1_domain[0], x1_domain[1]+1):
        for j in range(x2_domain[0], x2_domain[1]+1):
            x.append((i, j))
    
    return x


# making the y points    
def making_y_points1(x):
    y = []
    for i in x:
        r = my_function(i[0], i[1])
        f.write(f"{i[0]}, {i[1]} = {r}\n")
        y.append(r)
            
    return y


def my_function(x1, x2):
    # return (2*x1)+(3*x2)
    # return 3*(x1**2) - math.sin(x2)
    return math.sin(x1) * (x2**3)


if __name__ == "__main__":
    
    f = open('2D_in_out3.txt', 'w')

    f.write("our function is: sin(x1)*(x2**3) \n")

    x1_domain = (1, 10)
    x2_domain = (1, 10)
    x = making_x_points(x1_domain, x2_domain)
    y = making_y_points1(x)
    
    f.close() 