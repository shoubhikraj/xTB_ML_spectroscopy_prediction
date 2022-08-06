import pandas as pd
import os

def get_coord_from_xyz(fname):
    with open(fname,'r') as fha:
        xyztext = fha.readlines()
    coordblock = xyztext[2:]
    return coordblock

def dos2linux(fname):
    # convert dos to unix
    with open(new_name,'rb') as open_file:
        content = open_file.read()
    content = content.replace(WIN_LN_END,UNIX_LN_END)
    with open(new_name,'wb') as open_file:
        open_file.write(content)

def get_smd_solv_name(sol_name):
    sol_name = str(sol_name)
    if sol_name not in ['acetone', 'acetonitrile', 'benzene', 'carbon tetrachloride',\
       'chloroform', 'cyclohexane', 'dichloromethane', 'diethyl ether',\
       'dimethylformamide', 'dimethylsulfoxide', 'dioxane', 'ethanol',\
       'ethyl ethanoate', 'hexane', 'methanol', 'n-heptane', 'tetrahydrofuran',\
       'toluene', 'water']:
       raise Exception('Unknown solvent!')
    if sol_name=="dimethylformamide":
        return "n,n-dimethylformamide"
    elif sol_name=="dioxane":
        return "1,4-dioxane"
    elif sol_name=="hexane":
        return "n-hexane"
    else:
        return sol_name

with open('template.inp.txt','r') as fh:
    templ_text = fh.readlines()


line_num_found = False
for line_num in range(len(templ_text)):
    if templ_text[line_num].find('* xyz 0 1')!=-1:
        line_num_found = True
        break

if not line_num_found:
    raise Exception('Template file corrupted!')

WIN_LN_END = b'\r\n'
UNIX_LN_END = b'\n'

df = pd.read_csv('../benchmark_molecules.csv',index_col=0)
functional_list = ['x3lyp','pbe0','b2plyp','b2gp-plyp','m062x','b3lyp','wb97x-d3','wb2plyp']


for num,row in df.iterrows():
    xyzname = '../from_xtbopt/bench-'+str(num)+'.xyz'
    if not os.path.exists('bench-'+str(num)):
        os.mkdir('bench-'+str(num))
    print("processing",xyzname)
    coords = get_coord_from_xyz(xyzname)
    new_file_text_list = list(templ_text[0:line_num+1])+list(coords)+list(templ_text[line_num+1:])
    new_file_text = ''.join(new_file_text_list)
    this_solvent = get_smd_solv_name(row['solvent'])
    #print(get_smd_solv_name(row['solvent']))
    new_file_text = new_file_text.replace('mysolvent',this_solvent)
    for functional in functional_list:
        if functional == 'm06l' or functional == 'm062x':
            text_to_write = new_file_text.replace('functional',functional+' defgrid3')
        else:
            text_to_write = new_file_text.replace('functional',functional)
        if functional in ['b2plyp','wb2plyp','b2gp-plyp']:
            func_name = 'optpbed3-'+functional
            text_to_write = text_to_write.replace(functional,'pbe0 d3bj',1)
        else:
            func_name = functional
        new_name = 'bench-'+str(num)+'/'+func_name+'-train-'+str(num)+'.inp'
        with open(new_name,'w') as fh:
            fh.write(text_to_write)
        dos2linux(new_name)



    
