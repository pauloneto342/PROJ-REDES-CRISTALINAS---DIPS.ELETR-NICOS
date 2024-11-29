import numpy as np
import matplotlib.pyplot as plt

def generate_lattice_points(a, b, c, n=2):
    points = [i * a + j * b + k * c for i in range(n) for j in range(n) for k in range(n)]
    return np.array(points)

def plot_lattice(points, a_length, b_length=None, c_length=None, title="Lattice"):
    b_length = b_length or a_length
    c_length = c_length or a_length
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

   
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue')

    
    for p1 in points:
        for p2 in points:
            distance = np.linalg.norm(p1 - p2)
            if any(np.isclose(distance, d) for d in (a_length, b_length, c_length)):
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='gray')


    x_limits = (np.min(points[:, 0]), np.max(points[:, 0]))
    y_limits = (np.min(points[:, 1]), np.max(points[:, 1]))
    z_limits = (np.min(points[:, 2]), np.max(points[:, 2]))
    
    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_zlim(z_limits)

 
    max_range = np.array([x_limits[1] - x_limits[0], 
                          y_limits[1] - y_limits[0], 
                          z_limits[1] - z_limits[0]]).max() / 2.0

    mid_x = (x_limits[0] + x_limits[1]) / 2.0
    mid_y = (y_limits[0] + y_limits[1]) / 2.0
    mid_z = (z_limits[0] + z_limits[1]) / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show(block=False)

def plot_cubic_simple():
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.array([0, 0, 1])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length=1, title="Rede Cúbica Simples")

def plot_tetragonal_p(a_length=1, c_length=2):
    a = np.array([a_length, 0, 0])
    b = np.array([0, a_length, 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, c_length=c_length, title="Rede Tetragonal P")

def plot_orthorhombic_p(a_length=1, b_length=3, c_length=2):
    a = np.array([a_length, 0, 0])
    b = np.array([0, b_length, 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, b_length, c_length, title="Rede Ortorrômbica P")

def plot_monoclinic_p(a_length=5, b_length=7, c_length=6, beta=np.deg2rad(95)):
    a = np.array([a_length, 0, 0])
    b = np.array([b_length * np.cos(beta), b_length * np.sin(beta), 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, b_length, c_length, title="Rede Monoclínica P")

def plot_triclinic_p(a_length=1, b_length=3, c_length=2, alpha=np.deg2rad(86), beta=np.deg2rad(91), gamma=np.deg2rad(96)):
    a = np.array([a_length, 0, 0])
    b = np.array([b_length * np.cos(gamma), b_length * np.sin(gamma), 0])
    c = np.array([
        c_length * np.cos(beta),
        c_length * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma),
        c_length * np.sqrt(1 - (np.cos(alpha) ** 2) - (np.cos(beta) ** 2) - (np.cos(gamma) ** 2)
                           + 2 * np.cos(alpha) * np.cos(beta) * np.cos(gamma)) / np.sin(gamma),
    ])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, b_length, c_length, title="Rede Triclínica P")

def plot_trigonal_r(a_length=1, c_length=1, alpha=np.deg2rad(100)):
    a = np.array([a_length, 0, 0])
    b = np.array([a_length * np.cos(alpha), a_length * np.sin(alpha), 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, c_length=c_length, title="Rede Trigonal R")

def plot_trigonal_c(a_length=1, c_length=2, alpha=np.deg2rad(90), beta=np.deg2rad(90), gamma=np.deg2rad(120)):
    a = np.array([a_length, 0, 0])
    b = np.array([a_length * np.cos(gamma), a_length * np.sin(gamma), 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, c_length=c_length, title="Rede Trigonal C")

def plot_hexagonal_p(a_length=1, c_length=2):
    a = np.array([a_length, 0, 0])
    b = np.array([a_length * np.cos(np.deg2rad(120)), a_length * np.sin(np.deg2rad(120)), 0])
    c = np.array([0, 0, c_length])
    points = generate_lattice_points(a, b, c)
    plot_lattice(points, a_length, c_length=c_length, title="Rede Hexagonal P")

def main():
    plot_cubic_simple()
    plot_tetragonal_p()
    plot_orthorhombic_p()
    plot_monoclinic_p()
    plot_triclinic_p()
    plot_trigonal_r()
    plot_trigonal_c()
    plot_hexagonal_p()
    plt.show()

if __name__ == "__main__":
    main()
