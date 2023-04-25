import random
from sklearn.metrics import mean_squared_error
import math


# choosing the operator
def my_operator():
    op = ['+', '-', '*', '/', '**']
    return(random.choice(op))

def my_leaf():
    leaf = [random.randint(1, 9), 'x']
    return(random.choice(leaf))

def single_op(op):
    if(op=='sin' or op=='cos' or op=='tan' or op=='cot'):
        return True
    else: return False

class Node:
    # my node class 
    
    def __init__(self, _depth, _operator, _children = [], _is_leaf = False, _value = None):
        self.operator = _operator
        self.depth = _depth
        self.children = _children
        self.is_leaf = _is_leaf
        # value is the answer of a specific x (since this node)
        self.value = _value


class Tree:
    # my tree class

    def __init__(self, _max_depth):
        self.max_depth = _max_depth
        self.root = None
        self.in_order = None
        
    def _fit(self):
        self.root = self._grow_tree(self.max_depth)
        
    def _grow_tree(self, max_depth, CS = 2):
        
        depth = random.randint(0, max_depth)
          
        x = my_operator()
        if(single_op(x)): CS=1

        children = []
        
        if(depth==0):
            x = my_leaf()
        else:
            for i in range(CS):
                children.append(self._grow_tree(depth-1))

        n = Node(depth, x, children)
        if(depth==0): n.is_leaf = True
        return n
            

    def printTree (self):
        self.in_order = self.to_math_string(self.root)
        print(self.in_order)        

    
    def to_math_string(self, node):
        if node.is_leaf:
            return f"{node.operator}"
        else:
            if len(node.children) == 1:
                return f"{node.operator}({self.to_math_string(node.children[0])})"
            else:
                return f"({self.to_math_string(node.children[0])}{node.operator}{self.to_math_string(node.children[1])})"
            
                    
            
# making each of our trees
def tree_making(max_depth):  
    t = Tree(max_depth)
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
        t_y = calculator(tree.root, single_x, zero_flag)
        if(zero_flag or abs(t_y)>100000 or math.isinf(t_y) or math.isnan(t_y)):
            t_y = 100000
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
            right_val = 1

        return(
        ((root.operator == '+') and (left_val + right_val)) or
        ((root.operator == '-') and (left_val - right_val)) or
        ((root.operator == '*') and (left_val * right_val)) or
        ((root.operator == '/') and (left_val / right_val)) or
        ((root.operator == '**') and (left_val ** right_val)))