import numpy as np
import pandas as pd

columns = ['tree','mse']

tree = []
mse = []

# (tree_mse) is a tuple 
def printing(tree_mse):
    for i in tree_mse:
        tree.append(i[0])
        mse.append(i[1])
    df = pd.DataFrame(list(zip(tree, mse)), columns=columns)
        
# df = pd.DataFrame(list(zip(tree, mse)), columns=columns)