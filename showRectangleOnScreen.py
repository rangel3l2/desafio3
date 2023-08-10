import matplotlib.pyplot as plt   
 
def show_rectangle_on_screen():

    x_A = 63.932884668772836
    y_A = 96.42572804054143
    x_B = 63.932884668772836
    y_B = 115.30945508424092
    x_C = 90.5158815417008
    y_C = 115.30945508424092
    x_D = 90.5158815417008
    y_D = 96.42572804054143
    plt.figure()
    plt.plot([x_A, x_B, x_C, x_D, x_A], [y_A, y_B, y_C, y_D,y_A], marker='o')
    plt.xlim(0, 120)
    plt.ylim(0, 120)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Retângulo')
    plt.show()
    
show_rectangle_on_screen()