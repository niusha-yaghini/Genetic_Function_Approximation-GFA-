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

        
def calculator(root, x):
    if(root.is_leaf):
        if(root.operator == 'x'): 
            return x
        else: 
            return root.operator
    else:
        # we have not consider sin and cos
        
        left_val = calculator(root.children[0], x)
        right_val = calculator(root.children[1], x)

        divide_flag = False
        if(root.operator == '/' and right_val == 0):
            divide_flag = True
            right_val = 1

        power_flag = False
        if(left_val==0 and right_val<0):
            power_flag = True
            right_val = 1

        # overflow_flag = False
        # try:
        #     if(root.operator=="**"): x = left_val ** right_val
        #     if(root.operator=="*"): x = left_val * right_val
        #     if(root.operator=="/"): x = left_val / right_val
        # except OverflowError as e:
        #     overflow_flag = True

        try:
            return(
            ((root.operator == '+') and (left_val + right_val)) or
            ((root.operator == '-') and (left_val - right_val)) or
            ((root.operator == '*') and (left_val * right_val)) or
            ((root.operator == '/') and (not divide_flag) and (left_val / right_val)) or
            ((root.operator == '**') and (not power_flag) and (left_val ** right_val)))
        except OverflowError as e:
            return 100000
        
def _mse(tree, list_x, list_y):
    trees_y = []
    for single_x in list_x:
        t_y = calculator(tree.root, single_x)
        try:
            if(math.isinf(t_y) or math.isnan(t_y) or t_y>100000 or t_y<-100000):
                t_y = 100000
        except:
            t_y = 100000
        trees_y.append(t_y)
    mse = mean_squared_error(list_y, trees_y)
    return mse

        
def calculating_mse(tree_list, X, Y):
    i = 1
    mse_sum = 0
    best_mse = float('inf')
    for t in tree_list:
        t.mse = _mse(t, X, Y)
        mse_sum += t.mse
        if (t.mse<best_mse): best_mse = t.mse
        print(f"tree number {i} = {t.in_order} and its mse is = {t.mse}")
        i += 1

    return mse_sum/i, best_mse
    