import math
from sklearn.metrics import mean_squared_error
import tree

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

        # try:
        print("before return")
        return(
        ((root.operator == '+') and (left_val + right_val)) or
        ((root.operator == '-') and (left_val - right_val)) or
        ((root.operator == '*') and (left_val * right_val)) or
        ((root.operator == '/') and (not divide_flag) and (left_val / right_val)) or
        ((root.operator == '**') and (not power_flag) and (left_val ** right_val)))
        # except OverflowError as e:
        #     return 100000
        
max_depth = 2
amount_of_trees = 1
list_of_parents = tree.all_trees(amount_of_trees, max_depth)
list_of_parents[0].print_tree()
print(list_of_parents[0].in_order)
x = 5
t_y = calculator(list_of_parents[0].root, x)
# print("t_y", t_y)
# print("after calculator")
try:
    if(math.isinf(t_y) or math.isnan(t_y) or t_y>100000 or t_y<-100000):
        t_y = 100000
except:
    t_y = 100000

print(t_y)