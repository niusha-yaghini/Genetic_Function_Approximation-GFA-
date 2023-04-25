import numpy as np
from random import random
import math
import tree
import print_tree_mse

    
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
    f = open('in_out.txt', 'r')
    f.readline()
    X = []
    Y = []
    for i in range(domain):
        a = f.readline().split(',')
        X.append(int(a[0]))
        Y.append(int(a[1]))
        
    
    # making trees
    amount_of_trees = 40
    max_depth = 4
    
    # population zero
    list_of_trees = tree.all_trees(amount_of_trees, max_depth)
    print()
    
    # [(tree1, mse1), (tree2, mse2), ... ]
    tree_MSE = tree.all_mse(list_of_trees, X, Y)
    print()
    
    print_tree_mse.printing(tree_MSE)
    
    # choosing parent trees (with tonometer procedure)
    # list of (amount_of_trees / 2) couple trees
    # k parameter: choosing the best mse between random k tree
    # we have couple parents of just trees
    k = 3
    couple_parents = tonometer(tree_MSE, k)
    
    
    # probblity of doing cross-over
    # 70 percent of couples are going to cross over (the are going to change theirs nodes together randomly)
    pc = 0.7
    # children = cross_over(couple_parents, pc)
    
