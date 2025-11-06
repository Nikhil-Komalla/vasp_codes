from wulffpack import (SingleCrystal,
Decahedron,
Icosahedron)
from ase.build import bulk
from ase.io import read, write
import matplotlib.pyplot as plt


prim = read('POSCAR', format='vasp')

surface_energies = {(0, 0, 1): 1.00,
(0, 1,1): 1.51,
(1, 1, 1): 1.19}



particle = SingleCrystal(surface_energies,
primitive_structure=prim,
natoms=5000)

#colors = {(1, 0, 0): '#0053b5',
#(1, 1, 0): "#ddd726",
#(1, 1, 1): "#9538db"}

# This will now create an interactive plot
particle.view()
#particle.view(colors=colors)
