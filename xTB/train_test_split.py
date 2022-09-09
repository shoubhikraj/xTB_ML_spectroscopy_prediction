import pandas as pd


df = pd.read_csv('total_set_for_xTB.csv',index_col=0)

train = df.sample(n=2500,random_state=800)
train.reset_index(drop=True,inplace=True)
train.to_csv('train_dataset.csv')
test = df.drop(train.index)
test.reset_index(drop=True,inplace=True)
test.to_csv('test_dataset.csv')

#low_mw = train[train.mol_wt<400]
#low_mw.sample(n=13,random_state=200).to_csv('bench_remaining.csv')