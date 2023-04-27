import random
from sklearn.metrics import mean_squared_error
import math


# choosing the operator
def my_operator():
    op = ['+', '-', '*', '/', '**', 'sin', 'cos']
    return(random.choice(op))

# choosing the leaf
def my_leaf():
    leaf = [random.randint(1, 9), 'x']
    return(random.choice(leaf))

# checking type of function (1 child needed or 2 childs needed)
def single_op(op):
    if(op=='sin' or op=='cos' or op=='tan' or op=='cot'):
        return True
    else: 
        return False

class Node:
    # my node class 
    
    def __init__(self, _depth, _operator, _children = [], _is_leaf = False):
        self.operator = _operator
        self.depth = _depth
        self.children = _children
        self.is_leaf = _is_leaf

class Tree:
    # my tree class

    def __init__(self, _max_depth = None):
        self.max_depth = _max_depth
        self.root = None
        self.in_order = None
        self.mse = None        
        
    def _fit(self):
        self.root = self._grow_tree(self.max_depth)
        
    def _grow_tree(self, max_depth, CS = 2):
        
        # choosing a random depth each time (between 0 to max given depth)
        depth = random.randint(0, max_depth)
          
        # choosing the operator for current node
        x = my_operator()
        
        # check the type of our function and fix the amount of our children needed number
        if(single_op(x)):
            CS = 1
        else: 
            CS = 2

        children = []
        
        # building the tree base on current depth and children needed
        if(depth==0):
            x = my_leaf()
        else:
            for i in range(CS):
                children.append(self._grow_tree(depth-1))

        # making the node 
        n = Node(depth, x, children)
        if(depth==0): n.is_leaf = True
        return n          

    def print_tree (self):
        # making the inorder show of our tree
        
        self.in_order = self.to_math_string(self.root)
        print(self.in_order)        
   
    def to_math_string(self, node):
        if(node.is_leaf):
            return f"{node.operator}"
        else:
            if(len(node.children)) == 1:
                return f"{node.operator}({self.to_math_string(node.children[0])})"
            else:
                return f"({self.to_math_string(node.children[0])}{node.operator}{self.to_math_string(node.children[1])})"

def tree_making(max_depth):  
    # making each of our trees

    t = Tree(max_depth)
    t._fit()
    t.print_tree()
    print()
    return t     
        
def all_trees(amount, max_depth):
    # making a list of all random trees (generation 0)

    trees = []
    for i in range(amount):
        print(f"tree number {i+1} is: ")
        tree = tree_making(max_depth)
        trees.append(tree)
    return trees
        
# def calculator(root, x, flag):
#     # doing the calculating for each function that we have made with given input
#     if(flag):
#         return
    
#     if(root.is_leaf):
#         if(root.operator == 'x'): 
#             return x
#         else: 
#             return root.operator
#     else:
        
#         left_val = 1
#         right_val = 1
        
#         if(len(root.children)==1):
#             val = calculator(root.children[0], x, flag)
#         else:       
#             left_val = calculator(root.children[0], x, flag)
#             right_val = calculator(root.children[1], x, flag)

#         # checking for dividing error
#         if(root.operator == '/' and right_val == 0):
#             flag = True
#             return

#         # checking for power error
#         if(left_val == 0 and right_val < 0):
#             flag = True
#             return
        
#         # checking for making large numbers error
#         if(root.operator == '**'):
#             if(left_val>100000 or left_val<-100000 or right_val>100 or right_val<-100):
#                 flag = True
#                 return
                
#         try:
#             if(root.operator == '**'):
#                 a = left_val ** right_val
#         except:
#             flag = True
#             return
            
#         try:
#             return(
#             ((root.operator == 'sin') and (math.sin(val))) or
#             ((root.operator == 'cos') and (math.cos(val))) or
#             ((root.operator == '+') and (left_val + right_val)) or
#             ((root.operator == '-') and (left_val - right_val)) or
#             ((root.operator == '*') and (left_val * right_val)) or
#             ((root.operator == '/') and (left_val / right_val)) or
#             ((root.operator == '**') and (left_val ** right_val)))
#         except:
#             return 100000

def calculator(root, x, flag):
    # doing the calculating for each function that we have made with given input
    
    if(flag):
        return
    
    if(root.is_leaf):
        if(root.operator == 'x'): 
            return x
        else: 
            return root.operator
    else:
        
        if(len(root.children)==1):
            val = calculator(root.children[0], x, flag)
        else:       
            left_val = calculator(root.children[0], x, flag)
            right_val = calculator(root.children[1], x, flag)


        if (root.operator == 'sin'):
            return math.sin(val)
        elif (root.operator == 'cos'):
            return math.cos(val)
        elif (root.operator == '+'):
            return left_val + right_val
        elif (root.operator == '-'):
            return left_val - right_val
        elif (root.operator == '*'):
            left_val * right_val
        elif (root.operator == '/'):
            left_val / right_val
        elif (root.operator == '**'):
            return left_val ** right_val
        
        
def mean_abs_error(true_y, my_y):
    amount = len(my_y)
    sum = 0
    for i in range(amount):
        sum += abs(my_y[i]-true_y[i])
    return sum/amount
        
def _mse(tree, list_x, list_y):
    # calculating each tree mse with given inputs and outputs
    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = calculator(tree.root, single_x, flag)
        try:
            if(flag==True or math.isnan(t_y) or math.isinf(t_y) or t_y>100000 or t_y<-100000):
                t_y = 100000
        except:
            t_y = 100000
        trees_y.append(t_y)
    # mse = mean_squared_error(list_y, trees_y)
    mse = mean_abs_error(list_y, trees_y)
    return mse

def calculating_mse(tree_list, X, Y):
    # calculating the average-mse and best-mse for all of our trees and given inputs and outputs
    
    i = 1
    mse_sum = 0
    best_mse = float('inf')
    best_tree = None
    for t in tree_list:
        t.mse = _mse(t, X, Y)
        mse_sum += t.mse
        if (t.mse<best_mse):
            best_mse = t.mse
            best_tree = t
        print(f"tree number {i} = {t.in_order} and its mse is = {t.mse}")
        i += 1

    return mse_sum/i, best_mse, best_tree