import random
import tree
# from math import *

def my_operator():
    # op = {1: ['sin','cos','e','ln','tg','tanh','abs'], 2:['+', '-', '*', '/']}
    op = ['+', '-', '*', '/', 'sin', 'cos']
    # op2 = ['sin', 'cos', 'tan', 'cot']
    return(random.choice(op))

def tree_making(depth):
    if(depth == 1):
        return random.randint(0, 9)  # return a random number as a leaf node
    else:
        data = my_operator()
        children = []
        if(data == 'sin' or data == 'cos'):
            child = tree_making(depth-1)
            children.append(child)
            # if(depth!=2):
            #     print(f"depth is {depth}. only child is {child.data}")
            # else:
            #     print(f"depth is {depth}. only child is {child}")
        else:
            left_child = tree_making(depth-1)
            children.append(left_child)
            # if(depth!=2):
            #     print(f"depth is {depth}. left child is {left_child.data}")
            # else:
            #     print(f"depth is {depth}. left child is {left_child}")
            right_child = tree_making(depth-1)
            children.append(right_child)
            # if(depth!=2):
            #     print(f"depth is {depth}. right child is {right_child.data}")
            # else:
            #     print(f"depth is {depth}. right child is {right_child}")
        return(tree.Tree(data, children))


print("starting")
# t = tree.Tree("+")
my_tree = tree_making(4)
print()
