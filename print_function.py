import matplotlib.pyplot as plt
import tree

def result_one_D(t, list_x):    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = tree.calculator(t.root, single_x, flag)
        if(flag==True or t_y>100000 or t_y<-100000):
            t_y = 100000

        trees_y.append(t_y)
    return trees_y

def print_func_one_D(list_x, actual_y, predicted_tree, actual_f, predicted_f, photo_number):

    predicted_y = result_one_D(predicted_tree, list_x)

    fig, ax = plt.subplots()
    actual_function,  = plt.plot(list_x, actual_y, label='actual function')
    predicted_function, = plt.plot(list_x, predicted_y, label='predicted function')

    ax.set_title(f"actual function: {actual_f}, predicted function: {predicted_f}")
    ax.legend(handles=[actual_function, predicted_function])
    name = f"actual_predicted_function_{photo_number}_" + '.png'

    plt.savefig(name)
    plt.show()
    
    print()
    
def result_two_D(t, list_x):   
    two_D_flag = True 
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = tree.calculator(two_D_flag, t.root, single_x, flag)
        if(flag==True or t_y>100000 or t_y<-100000):
            t_y = 100000
        trees_y.append(t_y)
    return trees_y
    
    
def couple_to_list(list_x):
    x1 = []
    x2 = []
    for i in list_x:
        x1.append(i[0])
        x2.append(i[1])
        
    return x1, x2

    
def print_func_two_D(list_x, actual_y, predicted_tree, actual_f, predicted_f, photo_number):
    
    predicted_y = result_two_D(predicted_tree, list_x)

    list_x1, list_x2 = couple_to_list(list_x)

    fig = plt.figure(figsize = (8,8))
    ax = plt.axes(projection='3d')
    
    ax.scatter(list_x1, list_x2, actual_y, c='b', label='actual function')
    ax.scatter(list_x1, list_x2, predicted_y, c='r', label='predicted function')


    ax.set_title('actual function & predicted function')

    # Set axes label
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('y')
    
    ax.legend()
    name = f"actual_predicted_function_{photo_number}_" + '.png'

    plt.savefig(name)
    plt.show()