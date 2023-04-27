import numpy as np
import random as rnd
import math
import tree
import print_tree_mse
import copy

    
def change_node(child_root1, change_node1, child_root2, change_node2):
    
    queue1 = []
    queue1.append(child_root1)
    
    while change_node1!=None:
        node = queue1.pop()
        if(node!=change_node1):
            print("node.depth = ", node.depth)
            print("node.operator = ", node.operator)
            print("node.children = ", node.children)
            print("node.is_leaf = " , node.is_leaf)

            print("change_node1.depth = ", change_node1.depth)
            print("change_node1.operator = ", change_node1.operator)
            print("change_node1.children = ", change_node1.children)
            print("change_node1.is_leaf = ", change_node1.is_leaf)

            # print(change_node1.operator)
            # print(node.operator)
            # print(type(node))
            # print(type(change_node1))

            for i in range(len(node.children)):
                queue1.append(node.children[i])
        else:
            node = copy.deepcopy(change_node2)
            queue1.append(node)
            change_node1 = None
            
    queue2 = []
    queue2.append(child_root2)
            
    while change_node2!=None:
        node = queue2.pop()
        if(node!=change_node2):
            for j in range(len(node.children)):
                queue2.append(node.children[j])
        else:
            node = copy.deepcopy(change_node1)
            queue2.append(node)
            change_node2 = None
            
        
def make_list_node(root, nodes):
    nodes.append(root)
    if(len(root.children)!=0):
        for i in root.children:
            make_list_node(i, nodes)
                
    return nodes

    
def cross_over(parent1, parent2, pc):
    x = rnd.random()
    if(x<=pc):
        # making a list of all nodes
        nodes1 = []
        make_list_node(parent1.root, nodes1)
        nodes2 = []
        make_list_node(parent2.root, nodes2)
        
        # choosing a node to change
        change_node1 = rnd.choice(nodes1)
        change_node2 = rnd.choice(nodes2)

        print("parent1.in_order = ", parent1.in_order)
        print("parent2.in_order = ", parent2.in_order)

        print("change_node1.operator = ", change_node1.operator)
        print("change_node1.operator = ", change_node2.operator)


        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)        

        # making the child nodes with changing the nodes        
        change_node(child1.root, change_node1, child2.root, change_node2)
        
        print("child1.in_order = ", child1.in_order)
        print("child2.in_order = ", child2.in_order)

        
        return child1, child2

    else:
        return parent1, parent2
            
        
def tournament(p_trees, k):
    couple_parent = []
    for j in range(2):
        best_mse = float('inf')
        best_tree = None
        for z in range(k):
            t = rnd.choice(p_trees)  
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
        children.append(child1)
        children.append(child2)
    
    return children
  

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
    amount_of_trees = 20
    max_depth = 4
    
    # population zero
    list_of_parents = tree.all_trees(amount_of_trees, max_depth)
    print(len(list_of_parents))
    
    #add to each tree the mse property
    tree.calculating_mse(list_of_parents, X, Y)
    
    # choosing parent trees (with tonometer procedure)
    # list of (amount_of_trees / 2) couple trees
    # k parameter: choosing the best mse between random k tree
    # we have couple parents of just trees
    k = 3
    pc = 0.5 # the probblity of cross-over
    list_of_children = making_children(list_of_parents, k, pc)
    
