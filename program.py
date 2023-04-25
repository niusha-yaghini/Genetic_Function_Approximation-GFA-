import numpy as np
from random import random
import random
import math
import tree
import print_tree_mse


def tournament(p_trees, k):
    couple_parent = []
    for j in range(2):
        best_mse = float('inf')
        best_tree = None
        for z in range(k):
            t = random.choice(p_trees)  
            if(t.mse<best_mse):
                best_mse = t.mse
                best_tree = t
        couple_parent.append(best_tree)
    return couple_parent[0], couple_parent[1]

    

def making_children(parent_trees, k, pc):
    
    lenght = len(parent_trees)
    children = []
    
    for i in range(int(lenght/2)):
        #returning a couple of parents
        parent1, parent2 = tournament(parent_trees, k)        
        # we pass our couple to cross-over function(that 'pc' percent will do it)
        child1, child2 = cross_over(parent1, parent2, pc)
        

            
    
def cross_over(p1, p2, pc):
    x = random()
    if(x<=0.7):
        # picking a node from each parent
        node1 = random.choice(0, p1.node_amount)
        node2 = random.choice(0, p2.node_amount)
        # make new trees and change the choosen node to each other
    else:
        return p1, p2
            
            



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
    list_of_parents = tree.all_trees(amount_of_trees, max_depth)
    print()
    
    #add to each tree the mse property
    tree.calculating_mse(list_of_parents, X, Y)
    
    # choosing parent trees (with tonometer procedure)
    # list of (amount_of_trees / 2) couple trees
    # k parameter: choosing the best mse between random k tree
    # we have couple parents of just trees
    k = 3
    pc = 0.5 # the probblity of cross-over
    list_of_children = making_children(list_of_parents, k, pc)
    
