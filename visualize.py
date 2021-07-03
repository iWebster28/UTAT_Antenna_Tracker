###
# =================================
# 3D surface with polar coordinates
# =================================

# Demonstrates plotting a surface defined in polar coordinates.
# Uses the reversed version of the YlGnBu color map.
# Also demonstrates writing axis labels with latex math mode.

# Example contributed by Armin Moser.
###

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np


# def main():
#     # polar()
#     spherical()

# Demo polar system
def polar():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the mesh in polar coordinates and compute corresponding Z.
    r = np.linspace(0, 1.25, 50)
    p = np.linspace(0, 2*np.pi, 50)
    R, P = np.meshgrid(r, p)
    Z = ((R**2 - 1)**2)

    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(P), R*np.sin(P)

    # Plot the surface.
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

    # Tweak the limits and add latex math labels.
    ax.set_zlim(0, 1)
    ax.set_xlabel(r'$\phi_\mathrm{real}$')
    ax.set_ylabel(r'$\phi_\mathrm{im}$')
    ax.set_zlabel(r'$V(\phi)$')

    plt.show()

# Demo spherical system
def spherical(_phi, _theta):
    if _theta > 2 * np.pi:
        print("input pi large")
    if _phi > np.pi:
        print("input phi large")

    theta, phi = np.linspace(0, _theta, 40), np.linspace(0, _phi, 40)
    THETA, PHI = np.meshgrid(theta, phi)
    R = np.cos(PHI**2)
    X = R * np.sin(PHI) * np.cos(THETA)
    Y = R * np.sin(PHI) * np.sin(THETA)
    Z = R * np.cos(PHI)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    plot = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
        linewidth=0, antialiased=False, alpha=0.5)

    plt.show()

# Input: list of vectors in format: [x1, y1, z1, x2, y2, z2], where vector spans P_start = [x1, y1, z1] to P_end = [x2, y2, z2]
# Output: 3D Plot of vectors. Need to define x, y, and z ranges manually.
def vectors(vectors):
    print(vectors)
    soa = np.array(vectors)

    #https://stackoverflow.com/questions/40026718/different-colours-for-arrows-in-quiver-plot
    ph = np.linspace(0, 2*np.pi, 13)
    x = np.cos(ph)
    y = np.sin(ph)
    u = np.cos(ph)
    v = np.sin(ph)
    colors = np.arctan2(u, v)
    norm = Normalize()
    norm.autoscale(colors)
    colormap = cm.inferno
    # xyz: pt1, uvw: pt2
    # coordinates are behaving strange when plotted, so reverse Z and X, and W and U, even though we'll input vectors in the form
    # xyz and uvw
    X, Y, Z, U, V, W = zip(*soa)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, U, V, W, arrow_length_ratio=0.0000001, color=colormap(norm(colors))) #headwidth=1)
    # ax.set_xlim([-5, max([i[5] for i in vectors]) + 1]) # this logic needs to be changed
    # ax.set_ylim([-5, max([i[4] for i in vectors]) + 1])
    # ax.set_zlim([-5, max([i[3] for i in vectors]) + 1])
    ax.set_xlim([-5, 20]) # this logic needs to be changed
    ax.set_ylim([-5, 20])
    ax.set_zlim([-5, 20])
    plt.show()

# if __name__ == "__main__":
#     main()