import os
from pyxmolpp2 import Frame, PdbFile, rName, mName
import numpy as np

pdb_file = PdbFile("1t89.pdb")
frame = pdb_file.frames()[0]

chain_A_coords = frame.molecules.filter(mName == "A").coords.values[:2]
chain_C_coords = frame.molecules.filter(mName == "C").coords.values[:2]

a = 0
for i in chain_A_coords:
	for j in chain_C_coords:
		dist = np.linalg.norm(i-j)
		print(dist)