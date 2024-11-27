import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cubic_simple():
   
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.array([0, 0, 1])
    
  
    points = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                points.append(i * a + j * b + k * c)
    
    points = np.array(points)
    
   
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
 
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', label='Átomos')
    
    
    for p1 in points:
        for p2 in points:
            if np.linalg.norm(p1 - p2) == 1:  
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='gray')
    
    
    ax.set_title('Rede Cúbica Simples')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show(block=False)  
def plot_tetragonal_p(a_length=1, c_length=2):
  
    
    a = np.array([a_length, 0, 0])
    b = np.array([0, a_length, 0])
    c = np.array([0, 0, c_length])
    
   
    points = []
    for i in range(2):  
        for j in range(2):
            for k in range(2):
                points.append(i * a + j * b + k * c)
    
    points = np.array(points)
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
   
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', label='Átomos')
    
  
    for p1 in points:
        for p2 in points:
            distance = np.linalg.norm(p1 - p2)
            if np.isclose(distance, a_length) or np.isclose(distance, c_length):  
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='gray')
    
    
    ax.set_title('Rede Tetragonal P')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show(block=False)  


def main():
    
    plot_cubic_simple()
    
    
    plot_tetragonal_p()
    
    
    plt.show()


if __name__ == "__main__":
    main()