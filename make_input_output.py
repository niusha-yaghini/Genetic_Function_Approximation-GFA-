import numpy as np

# making the x points
def making_x_points(domain):
    x = []
    for i in range(domain):
        x.append(i+1)
    return x

# making the y points    
def making_y_points(x):
    y = [((2*i)+3) for i in x]
    return y

def making_y_points2(x):
    y = [(i**3) for i in x]
    return y


if __name__ == "__main__":
    
    f = open('in_out2.txt', 'w')

    f.write("our function is: (x**3) \n")

    domain = 20
    x = making_x_points(domain)
    y = making_y_points2(x)
    
    for i in range(domain):
        f.write(f"{x[i]}, {y[i]}\n")
        
    f.close() 