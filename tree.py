# class Node:
#     # my node class 
    
#     def __init__(self, _operand, _children = None, _value = False):
#         self.operand = _operand
#         self.children = _children
#         self.value = _value
    
#     def is_leaf(self):
#         return self.value


class Tree:
    # my tree class

    def __init__(self, _data, _children = []):
        self.data = _data
        self.children = _children
    
    # def __init__(self, _data, _leftChild = None, _rightChild = None):
    #     self.data = _data
    #     self.leftChild = _leftChild
    #     self.rightChild = _rightChild
