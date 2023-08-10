import matplotlib.pyplot as plt   
 
def show_rectangle_on_screen():

    x_A = 44.55944263345067
    y_A = 5.549246224142124
    x_B = 12.504432285866962
    y_B = 61.15696406525164
    x_C = 60.86490375666338
    y_C = 92.29410567313512
    x_D = 98.24413391148128
    y_D = 25.7003314824266
    plt.figure()
    plt.plot([x_A, x_B, x_C, x_D, x_A], [y_A, y_B, y_C, y_D,y_A], marker='o')
    plt.xlim(0, 120)
    plt.ylim(0, 120)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Retângulo')
    plt.show()
    
show_rectangle_on_screen()