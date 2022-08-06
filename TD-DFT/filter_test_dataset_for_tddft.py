import pandas as pd
import json
import shutil

df_test = pd.read_csv('test_dataset.csv',index_col=0)

df_filtered = df_test[df_test.mol_wt < 400]

df_filtered = df_filtered.sample(n=200,random_state=200)

df_filtered.to_csv('filtered_test_dataset.csv')

filtered_indices = list(df_filtered.index)
with open('filtered_numbers.json','w') as fh:
    json.dump(filtered_indices, fh, indent=2)

for i in filtered_indices:
    shutil.copyfile('../xTB/test/std_xtb_run/test-'+str(i)+'.xyz','./test/from_xtb_opt/test-'+str(i)+'.xyz')
