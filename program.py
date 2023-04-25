import numpy as np
from random import random
import math
import tree


# making each of our trees
def tree_making(max_depth):  
    t = tree.Tree(max_depth)
    t._fit()
    t.printTree()
    print()
    return t
    
# making a list of all random trees
def all_trees(amount, max_depth):
    trees = []
    for i in range(amount):
        print(f"tree number {i+1} is: ")
        tree = tree_making(max_depth)
        trees.append(tree)
    return trees

def all_mse(tree_list, X, Y):
    trees_mse = []
    for t in tree_list:
        t_mse = _mse(t, X, Y)
        print(f"tree = {t.in_order} and its mse = {t_mse}", )
        trees_mse.append((t, t_mse))
    return trees_mse
            
        
def _mse(tree, list_x, list_y):
    trees_y = []
    for single_x in list_x:
        zero_flag = False
        t_y = 0
        # print(tree.in_order)
        # print("single x is :", single_x)
        t_y = calculator(tree.root, single_x, zero_flag)
        # print("my t_y is: ", t_y)
        # if(math.isnan(t_y)):
        #     print()
        if(zero_flag or abs(t_y)>100000):
            t_y = 100000
        # print("y is: ", t_y)
        trees_y.append(t_y)
    mse = mean_squared_error(list_y, trees_y)

    return mse

    
def calculator(root, x, _flag):
    if(root.is_leaf):
        if(root.operator == 'x'): 
            return x
        else: 
            return root.operator
    else:
        # we have not consider sin and cos
        left_val = calculator(root.children[0], x, _flag)
        right_val = calculator(root.children[1], x, _flag)
        if(root.operator == '/' and right_val == 0):
            _flag = True
        if(left_val>100000 or right_val> 100000):
            _flag = True
        # if(math.isnan(left_val) or math.isnan(right_val)):
        #     print()
        
        if (root.operator == '+'): return left_val + right_val
        elif(root.operator == '-'): return left_val - right_val
        elif(root.operator == '*'): return left_val * right_val
        elif(root.operator == '/'): return left_val / right_val
        elif(root.operator == '**'): return left_val ** right_val


    
def tonometer(tree_mse, k):
    
    lenght = len(tree_mse)
    tt = tree_mse
    couple_parents = []
    
    for i in range(int(lenght/2)):
        # each couple
        for j in range(2):
            k = []
            #adding 3 random trees in k
            for z in range(k):
                t = random.choice(tt)  
                k.append(t)
            # how to choose the one with min mse???
        #how to make a couple ??? (of just the trees)
    # adding each couple to our list
            
    
def cross_over(parents, pc):
    for p in parents:
        x = random()
        if(x<=0.7):
            co(p)
            
            
def co(couple):
    t1 = couple[0]
    t2 = couple[1]
    


if __name__ == "__main__":
    
    # using domain
    domain = 20
    f = open('in&out.txt', 'r')
    f.readline()
    X = []
    Y = []
    for i in range(domain):
        a = f.readline().split(',')
        X.append(a[0])
        Y.append(int(a[1]))
        
    
    # making trees
    amount_of_trees = 40
    max_depth = 6
    
    # population zero
    list_of_trees = all_trees(amount_of_trees, max_depth)
    print()
    
    # [(tree1, mse1), (tree2, mse2), ... ]
    tree_MSE = all_mse(list_of_trees, X, Y)
    print()
    
    # choosing parent trees (with tonometer procedure)
    # list of (amount_of_trees / 2) couple trees
    # k parameter: choosing the best mse between random k tree
    # we have couple parents of just trees
    k = 3
    couple_parents = tonometer(tree_MSE, k)
    
    
    # probblity of doing cross-over
    # 70 percent of couples are going to cross over (the are going to change theirs nodes together randomly)
    pc = 0.7
    children = cross_over(couple_parents, pc)
    
