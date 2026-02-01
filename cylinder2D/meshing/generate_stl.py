"""
This script generates an STL file of a cylinder starting with a set of points
that form a circle in the z=0 plane. The points must be listed in clockwise
order and also that the first point is already duplicated as the last point.

Jonathan Eastridge
Last update: 29 January 2026
"""


import numpy as np

R = 0.25 # sphere radius
Npoints = 100
Npanels = Npoints - 1

theta = np.linspace(0, 2*np.pi, Npoints)
x = R * np.cos(theta)
y = R * np.sin(theta)

khat = np.array([0, 0, 1])
z = 0
dz = 0.1 # determines the span (irrelevant for 2D OpenFOAM simulation, but must be nonzero)

with open("cylinder.stl", "w") as f:
    f.write("solid test\n")

    for i in range(Npanels):
        v = np.array([x[i+1] - x[i], y[i+1] - y[1], z])
        normal = np.cross(v, khat)
        f.write("facet normal {:.6f} {:.6f} {:.6f}\n".format(*normal))
        f.write("  outer loop\n")
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i], y[i], z))
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i+1], y[i+1], z))
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i], y[i], dz))
        f.write("  endloop\n")
        f.write("endfacet\n")

    for i in range(Npanels):
        v = np.array([x[i+1] - x[i], y[i+1] - y[1], z])
        normal = np.cross(v, khat)
        f.write("facet normal {:.6f} {:.6f} {:.6f}\n".format(*normal))
        f.write("  outer loop\n")
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i+1], y[i+1], z))
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i+1], y[i+1], dz))
        f.write("    vertex {:.6f} {:.6f} {:.6f}\n".format(x[i], y[i], dz))
        f.write("  endloop\n")
        f.write("endfacet\n")

    f.write("endsolid\n")
