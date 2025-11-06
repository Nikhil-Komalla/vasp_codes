import os
from wulffpack import SingleCrystal, Decahedron, Icosahedron
from ase.io import read

# Assume program is running in the directory with POSCAR
default_poscar_path = os.path.join(os.getcwd(), 'POSCAR')

# Inform user that POSCAR will be searched in current folder
print(f"Looking for 'POSCAR' in the current directory: {os.getcwd()}")
print("Press Enter to use 'POSCAR' in current directory, or specify a different file.")

# Option to override POSCAR filename
poscar_filename = input(f"Enter POSCAR filename (default: POSCAR): ").strip()
poscar_path = poscar_filename if poscar_filename else default_poscar_path

# Load the structure
structure = read(poscar_path, format='vasp')

# Shape selection with options
print("\nChoose shape for Wulff construction:")
print("1. SingleCrystal")
print("2. Decahedron")
print("3. Icosahedron")
choice = input("Enter choice number: ").strip()

if choice == '1':
    shape_class = SingleCrystal
elif choice == '2':
    shape_class = Decahedron
elif choice == '3':
    shape_class = Icosahedron
else:
    print("Invalid choice, defaulting to SingleCrystal.")
    shape_class = SingleCrystal

# Input surface facets and energies
surface_energies = {}
print("\nEnter surface facets and energies in format 'h k l energy' (or Enter to finish):")
while True:
    inp = input("Facet (h k l energy): ").strip()
    if not inp:
        break
    try:
        h, k, l, energy = inp.split()
        surface_energies[(int(h), int(k), int(l))] = float(energy)
    except:
        print("Invalid format, try again.")

# Number of atoms
while True:
    natoms_input = input("Number of atoms in the particle (press Enter to use POSCAR's atom count): ").strip()
    if natoms_input == '':
        natoms = len(structure)
        print(f"Using atom count from POSCAR: {natoms}")
        break
    try:
        natoms = int(natoms_input)
        break
    except ValueError:
        print("Please enter a valid integer or press Enter.")
        print("Invalid number, try again.")

# Create the shape
particle = shape_class(surface_energies, primitive_structure=structure, natoms=natoms)

# Visualize
particle.view()
