import numpy as np
import random as rnd
import math
import tree
import print_tree_mse
import copy
import matplotlib.pyplot as plt
    
def change_node(child_root1, change_node1, child_root2, change_node2):
    # change the specific node1 in tree1 with the specific node2 in tree2 with each other
    #       and making new trees as children
    
    queue1 = []
    queue1.append(child_root1)
    
    # making a cope of node1, because we will lose it after we change it with node2
    cn1 = copy.deepcopy(change_node1)
    
    # searching in tree1 untill we find our specific node, and changing it with node2
    flag1 = True
    while flag1:
        node = queue1.pop()
        if(node!=change_node1):
            for i in range(len(node.children)):
                queue1.append(node.children[i])
        else:
            node.depth = change_node2.depth
            node.operator = change_node2.operator
            node.children = copy.deepcopy(change_node2.children)
            node.is_leaf = change_node2.is_leaf
            flag1 = False
            
    queue2 = []
    queue2.append(child_root2)
         
    # searching in tree2 untill we find our specific node, and changing it with node1 (cn1)  
    flag2 = True
    while flag2:
        node = queue2.pop()
        if(node!=change_node2):
            for j in range(len(node.children)):
                queue2.append(node.children[j])
        else:
            node.depth = cn1.depth
            node.operator = cn1.operator
            node.children = copy.deepcopy(cn1.children)
            node.is_leaf = cn1.is_leaf
            flag2 = False          
        
def make_list_node(root, nodes):
    # making a list of all nodes in our tree
    
    nodes.append(root)
    if(len(root.children)!=0):
        for i in root.children:
            make_list_node(i, nodes)
                
    return nodes

def cross_over(parent1, parent2, pc):
    # doing the cross-over with the given cross-over-rate (pc), on 2 tree
    
    x = rnd.random()
    if(x<=pc):

        # making the child nodes for changing nodes        
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)        
        
        # making a list of all nodes
        nodes1 = []
        make_list_node(child1.root, nodes1)
        nodes2 = []
        make_list_node(child2.root, nodes2)
        
        # choosing a node to change
        change_node1 = rnd.choice(nodes1)
        change_node2 = rnd.choice(nodes2)
        
        # print("parent1.in_order = ", parent1.in_order)
        # print("parent2.in_order = ", parent2.in_order)

        # print("change_node1.operator (before change) = ", change_node1.operator)
        # print("change_node2.operator (before change) = ", change_node2.operator)

        change_node(child1.root, change_node1, child2.root, change_node2)

        child1.print_tree()
        child2.print_tree()

        # print("parent1.in_order = ", parent1.in_order)
        # print("parent2.in_order = ", parent2.in_order)

        # print("change_node1.operator (after change) = ", change_node1.operator)
        # print("change_node2.operator (after change) = ", change_node2.operator)
        
        return child1, child2
    
    else:
        return parent1, parent2
                   
def tournament(p_trees, k):
    # using the tournament preceture for selecting a couple tree
    # in this method we choose 3 tree randomly 2 times (2 times becuase we want a couple), and select the best-mse tree
    
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
    # we want to make children on base of a list of trees (parent_trees)
    
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
    
    # parameters
    domain = 20

    amount_of_trees = 100
    max_depth = 6

    k = 3 # k tournoment parameter
    pc = 0.5 # the probblity of cross-over

    amount_of_generations = 10 

    
    # using domain
    f = open('in_out3.txt', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(domain):
        a = f.readline().split(',')
        X.append(int(a[0]))
        Y.append(int(a[1]))
        
        
    # population number zero
    list_of_parents = tree.all_trees(amount_of_trees, max_depth)
    parents_average_mse, parents_best_mse, best_tree = tree.calculating_mse(list_of_parents, X, Y)
    
    # making lists for showing 
    x_generation_number = []
    y_average_of_each = []
    y_best_mse_of_each = []
    y_best_of_all = []
    y_best_tree = []
    
    for i in range(amount_of_generations):
    
        list_of_children = making_children(list_of_parents, k, pc)
        average_mse, best_mse, best_tree = tree.calculating_mse(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        x_generation_number.append(i)
        y_best_tree.append(best_tree)
        y_best_mse_of_each.append(best_mse)
        y_best_of_all.append(min(y_best_mse_of_each))
        y_average_of_each.append(average_mse)

    final_best_tree = None
    mse = float('inf')
    for i in y_best_tree:
        if i.mse<mse:
            final_best_tree = i
            mse = i.mse

    fig, ax = plt.subplots()
    best_of_each,  = plt.plot(x_generation_number, y_best_mse_of_each, label='best of this generation',  linewidth=3)
    best_of_all, = plt.plot(x_generation_number, y_best_of_all, label='best of all generations since now')

    ax.set_title(f"function = {given_function}, population = {amount_of_trees}")
    ax.legend(handles=[best_of_each, best_of_all])
    name = "result_8_" + str(amount_of_trees) + '.png'

    print("the function that my genetic believes: ", final_best_tree.in_order)

    plt.savefig(name)
    plt.show()
    
    print()
    
    fig, ax = plt.subplots()
    average_of_each, = plt.plot(x_generation_number, y_average_of_each, label='average of this generation')
    ax.set_title("function approximation with genetic")
    ax.legend(handles=[best_of_each, best_of_all])
    name = "average_" + str(1) + '.png'

    plt.savefig(name)
    plt.show()


    # we have not use sin and cos yet
    # for now the new generation is the children
    # we have not done mutation yet

    print()