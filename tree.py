import random

# choosing the operator
def my_operator():
    op = ['+', '-', '*', '/', 'sin', 'cos']
    return(random.choice(op))

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

    def __init__(self, _depth):
        self.depth = _depth
        self.root = None
        
    def _fit(self):
        self.root = self._grow_tree(self.depth)
        
    def _grow_tree(self, depth, CS = 2):
            
        x = my_operator()
        
        if (x=='sin' or x=='cos'):
            CS = 1
        
        children = []

        if(depth==1):
            if(CS==1):
                children=['x']
            else:
                children.append('x')
                children.append(random.randint(0, 9))
        else:
            for i in range(CS):
                children.append(self._grow_tree(depth-1))
                        
        n = Node(depth, x, children)
        if(depth==1): n.is_leaf = True
        return n
            
    def printTree (self):
        # print("printing the whole tree")
        print(self.to_math_string(self.root))
    
    def to_math_string(self, node):
        if node.is_leaf:
            if len(node.children) == 1:
                return f"{node.operator}({node.children[0]})"
            else:
                return f"({node.children[0]}{node.operator}{node.children[1]})"
        else:
            if len(node.children) == 1:
                return f"{node.operator}({self.to_math_string(node.children[0])})"
            else:
                return f"({self.to_math_string(node.children[0])}{node.operator}{self.to_math_string(node.children[1])})"