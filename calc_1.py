import os
from pyxmolpp2 import Frame, PdbFile, rName, mName
import numpy as np

pdb_file = PdbFile("1t89.pdb")
frame = pdb_file.frames()[0]

chain_A_coords = frame.molecules.filter(mName == "A").coords.values[:2]
chain_C_coords = frame.molecules.filter(mName == "C").coords.values[:2]


for i in chain_A_coords:
	for j in chain_C_coords:
 		a = np.sum((i-j)**2, axis = 0)
 		print(a**0.5)
