from Bio.PDB import PDBParser
import nglview as nv

# PDB dosyasını analiz etme
parser = PDBParser()
structure = parser.get_structure('1FAT', 'pdb1fat.ent')

# Görselleştirme
view = nv.show_biopython(structure)
view
