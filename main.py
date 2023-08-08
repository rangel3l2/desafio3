import numpy as np

resultado  = np.sqrt(4)
teste= resultado* -1

pontos = np.array([[1,1],[5,1],[1,5],[5,5]])
def calc(pontos):
    a = pontos[0]
    b = pontos[1]   
    c = pontos[2]
    d = pontos[3]  
    retaA = np.dot(a,b)
    retaB = np.dot(c,d)
    retaC = np.dot(a,c)
    retaD = np.dot(b,d)    
    resulted = np.dot(b,a) 
    print(resulted)
calc(pontos)