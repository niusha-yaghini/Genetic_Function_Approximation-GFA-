import numpy as np
import random
import math
import tree

# choosing operand
def my_operator():
    # op = {1: ['sin','cos','e','ln','tg','tanh','abs'], 2:['+', '-', '*', '/']}
    op = ['+', '-', '*', '/']
    return(random.choice(op))

# making the result function
def my_function(domain):
    result = [(4(i^2)+5(i)+3) for i in domain]
    return result

# making the x points
def making_x_points(points, domain):
    x = np.linspace(domain[0], domain[1], points)
    return x

# making the y points    
def making_y_points(x):
    y = np.array(my_function(x))
    return y

# making each of our trees
def tree_making(depth):  
    t = tree.Tree(depth)
    t._fit()
    print(t.root.is_leaf)
    t.printTree()
    return t  

# making a list of all random trees
def all_trees(amount, range):
    trees = []
    for i in range(amount):
        depth = random.randint(range[0], range[1])
        tree = tree_making(depth)
        trees.append(tree)
    return trees


if __name__ == "__main__":
    
    # making the train points
    points = 20
    domain = (-10, 10)
    
    X = making_x_points(points, domain)
    Y = making_y_points(X)
    
    # making trees
    amount_of_trees = 20
    range_of_depth = (3, 6)
    
    list_of_trees = all_trees(amount_of_trees, range_of_depth)
