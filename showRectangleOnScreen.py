import matplotlib.pyplot as plt   
 
def show_rectangle_on_screen():
    x_A = 84.91738363939314 
    y_A = 34.239075557711814
    x_B = 85.20968724670608
    y_B = 56.69875679720276
    x_C = 85.1913780870189
    y_C = 84.59100839668218
    x_D = 83.17519082097465
    y_D = 62.07686998718201
 
    plt.figure()
    plt.plot([x_A, x_B, x_C, x_D, x_A], [y_A, y_B, y_C, y_D,y_A], marker='o')
    plt.xlim(0, 120)
    plt.ylim(0, 120)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Retângulo')
    plt.show()
    
show_rectangle_on_screen()