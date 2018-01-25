import pandas as pd
pd.set_option('max_columns', 50)
pd.set_option('display.width', 200)
df = pd.read_csv('wzrost.txt', sep=";")
df['przyrost'] = df['19lat']/df['dlugosc_ur'] * 100

# print(df['przyrost'].idxmax()+1, df['przyrost'].max()) #5.1
# print(df.groupby(['plec']).mean().diff() > 1) #5.2
# print(df[df['15lat'] == df['19lat']]) #5.3


przyrost_col = df.columns.tolist()[2:-1]

for i, col in enumerate(przyrost_col):
    if i:
        df['przyrost_'+col] = df[przyrost_col[i]] - df[przyrost_col[i-1]]

print( df.groupby('plec').mean() ) #5.4

# 5.6
_6 = df[df['plec'] == 'ch'].median().to_csv('wynik6.txt')
