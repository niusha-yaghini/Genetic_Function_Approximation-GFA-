import math
import

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
        return(
        ((root.operator == '+') and (left_val + right_val)) or
        ((root.operator == '-') and (left_val - right_val)) or
        ((root.operator == '*') and (left_val * right_val)) or
        ((root.operator == '/') and (not divide_flag) and (left_val / right_val)) or
        ((root.operator == '**') and (not power_flag) and (left_val ** right_val)))
        # except OverflowError as e:
        #     return 100000
        
def _mse(tree, list_x, list_y):
    trees_y = []
    for single_x in list_x:
        # print("before calculator")
        t_y = calculator(tree.root, single_x)
        # print("after calculator")
        try:
            if(math.isinf(t_y) or math.isnan(t_y) or t_y>100000 or t_y<-100000):
                t_y = 100000
        except:
            t_y = 100000
        trees_y.append(t_y)
    mse = mean_squared_error(list_y, trees_y)
    return mse

_mse()