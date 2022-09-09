This folder contains all of the output files used for the test set of 633 dye like molecules. The efficiency of the trained model is tested on these molecules. To run the calculations on those molecules from scratch delete all of the molfiles and output files, and then do the following in order:

1. run ./generated_molfiles/generate_mol.py => this reads xTB/test_dataset.csv and generates molfiles from SMILES using RDKit. (The python packages pandas and rdkit must be installed) However, RDKit fails to generate 3D coordinates on some molecules: #255, #256, #395, #402, #440, #626. For these molecules only 2D coordinate is generated, I manually fixed them with Avogadro (open the molfile with Avogadro, it will prompt for generating 3D coords, then Save As...), but other softwares can be used as well.

2. run ./preliminary_ff_opt/optimize-with-gfnff.sh => this is a bash script, and it uses GFN-FF force field provided by xTB software to do a preliminary optimization

3. run ./final_xtb_opt/optimize-with-xtb.sh => this is not a bash script, it is job submission script for SGE job scheduler (because of the large number of molecules, I used the cluster), and it performs the final optimization with GFN2-xTB semi-empirical method, also uses xTB software

4. run ./std_xtb_run/mol_to_xyz.sh, and then run-all-script.sh in the same folder => the first bash script converts molfiles to xyz (requires openbabel) and the second is an SGE job script that runs xtb4stda and stda. The *.out files generated are the outputs from stda software (This is for sTD-xTB run i.e. full sTD-DFT treatment on xTB hamiltonian)
