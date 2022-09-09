The benchmark_molecules.csv files contains the molecules used for benchmarking, containing 20 randomly selected molecules from the training set and their absorption peaks. The column "lambda_max_exp_nm" contained the experimentally recorded absorption wavelengths in nanometres, while the "abs_max_ev" column contains the absorption maxima in eV units, converted from nm. To run the calculations on those molecules from scratch delete all of the molfiles and output files, and then do the following in order:

1. run ./generated_molfiles/generate_mol.py => this generated molfiles from SMILES using RDKit. (The python packages pandas and rdkit must be installed)

2. run ./preliminary_ff_opt/optimize-with-gfnff.sh => this is a bash script, and it uses GFN-FF force field provided by xTB software to do a preliminary optimization

3. run ./final_xtb_opt/optimize-with-xtb.sh => this script performs the final optimization with GFN2-xTB semi-empirical method, also uses xTB software

4. run ./std_xtb_run/mol_to_xyz.sh, and then run-all-script.sh in the same folder => the first script converts molfiles to xyz (requires openbabel) and the second script runs xtb4stda and stda. The *.out files generated are the outputs from stda software (This is for sTD-xTB run i.e. full sTD-DFT treatment on xTB hamiltonian)

5. copy all *.xyz files from ./std_xtb_run/ folder into ./stda_run/ folder, then run ./stda_run/run-all-stda.sh => this does the same calculation, but instead with sTDA-xTB method i.e. Tamm-Dancoff approximation on xTB hamiltonian
