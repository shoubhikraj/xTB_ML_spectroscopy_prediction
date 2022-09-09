from rdkit.Chem import rdmolfiles
import rdkit.Chem
import rdkit.Chem.AllChem
import pandas as pd


df = pd.read_csv('../../test_dataset.csv',index_col=0)

for index in range(len(df)): 
    molecule = rdkit.Chem.MolFromSmiles(df['SMILES'][index])
    print(df['SMILES'][index])
    mol_3d = rdkit.Chem.AddHs(molecule)
    rdkit.Chem.AllChem.EmbedMolecule(mol_3d,randomSeed=200,enforceChirality=True)
    filename = 'pre-test-'+str(index)+'.mol'
    rdmolfiles.MolToMolFile(mol_3d,filename)

