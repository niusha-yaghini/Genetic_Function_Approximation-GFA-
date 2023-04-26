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
        children.append(child1)
        children.append(child2)
    
    return children
        

def change_node(parent_root1, change_node1, parent_root2, change_node2):

    child1 = tree.Tree()
    child2 = tree.Tree()
    
    
    # while(i!=change_node1):
        
        
        # child1.root = root1
        # i+=1
        
        
# def BFSearch(self, n):  

#     # Initially marking all vertices as not visited  
#     visited_vertices = ( len(self.graph ))*[False]  

#     # creating a queue for visited vertices  
#     queue = []  

#     # setting source node as visited and adding it to the queue  
#     visited_vertices[n] = True  
#     queue.append(n)  
        

#     while queue:  

#         # popping the element from the queue which is printed  
#         n = queue.pop(0)  
#         print (n, end = " ")  

#         # getting vertices adjacent to the vertex n which is dequed.   
#         for v in self.graph[ n ]:  
#             if visited_vertices[v] == False:  
#                 queue.append(v)  
#                 visited_vertices[v] = True  

          
def make_list_node(root, nodes):
    
    if(len(root.children)!=0):
        for i in root.children:
            nodes.append(i)
            make_list_node(i, nodes)
                
    return nodes
        
        
        
    
def cross_over(parent1, parent2, pc):
    x = random()
    if(x<=pc):
        # making a list of all nodes
        nodes1 = []
        make_list_node(parent1.root, nodes1)
        nodes2 = []
        make_list_node(parent2.root, nodes2)
        
        # choosing a node to change
        change_node1 = random.choice(nodes1)
        change_node2 = random.choice(nodes2)


        # making the child nodes with changing the nodes        
        child1, child2 = change_node(parent1.root, change_node1, parent2.root, change_node2)
        
        return child1, child2

    else:
        return parent1, parent2
            
            

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
    
