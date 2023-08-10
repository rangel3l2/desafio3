import numpy as np
def calculate_angle(p1, encontro, p2):  
    vet1 = np.array(p1) - np.array(encontro)
    vet2 = np.array(p2) - np.array(encontro)
    cos = np.dot(vet1, vet2) / (np.linalg.norm(vet1) * np.linalg.norm(vet2))   
    rad = np.arccos(cos)  
    deg = np.degrees(rad)
    return deg
