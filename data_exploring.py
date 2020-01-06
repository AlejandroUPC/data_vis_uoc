import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go

df=pd.read_csv(r'pax_all_agreements_data.csv',sep=',')
df['Dat_Y'],df['Dat_M'],df['Dat_D']=df['Dat'].str.split('-').str

fecha_inicio=min(df['Dat_Y'])
fecha_final=max(df['Dat_Y'])


df_grupo_region_fecha=df.groupby(['Dat_Y','Reg'],as_index=False).size().reset_index()
df_group_region_mid=df_grupo_region_fecha[df_grupo_region_fecha['Reg'].str.contains('Middle East')]
df_group_region_eur=df_grupo_region_fecha[df_grupo_region_fecha['Reg'].str.contains('Europe')]
df_group_region_eur.rename(columns={0:'a'},inplace=True)
df_group_region_eur.a=pd.to_numeric(df_group_region_eur.a)
print(df_group_region_eur.dtypes)
df_group_region_eur.plot.bar(x='a',y='Dat_Y')


df['Reg'].value_counts().plot(kind='bar')
df.Dat_Y=pd.to_numeric(df.Dat_Y)
print(df.dtypes)
ax=df['Dat_Y'].value_counts().sort_index().plot(kind='bar',figsize=(10,4))
ax=df['Dat_M'].value_counts().sort_index().plot(kind='bar')

regions_evolution = pd.crosstab(df['Dat_Y'],df['Reg'])
regions_evolution.plot(color=sns.color_palette('Set2',12),figsize=(18,8))
plt.show()


#plt.figure(figsize = (12,4))
#plt.subplot(121)
#sns.distplot(x=df.dat_Y, kde = False, bins = 25)
#plt.subplot(122)
#sns.distplot(df['Dat_m'], kde = False)



layout = dict(title_text='Mentions of Crime in Peace Treaties over time',
             barmode = 'stack')
data = [
    go.Bar(name='Corruption', x=df[df['Cor'] >= 1].groupby('Dat_Y').count()['Con'].index, y=df[df['Cor'] >= 1].groupby('Dat_Y').count()['Con'].values),
    go.Bar(name='Terrorism', x=df[df['Terr'] >= 1].groupby('Dat_Y').count()['Con'].index, y=df[df['Terr'] >= 1].groupby('Dat_Y').count()['Con'].values),
    go.Bar(name='Organised Crime', x=df[df['SsrCrOcr'] >= 1].groupby('Dat_Y').count()['Con'].index, y=df[df['SsrCrOcr'] >= 1].groupby('Dat_Y').count()['Con'].values),
    go.Bar(name='Drugs', x=df[df['SsrDrugs'] >= 1].groupby('Dat_Y').count()['Con'].index, y=df[df['SsrDrugs'] >= 1].groupby('Dat_Y').count()['Con'].values),
]
fig = go.Figure(data=data, layout = layout)
fig.show()

"""
"""
df['InclRati']=df['GCh']+df['GDis']+df['GAge']+df['GMig']+df['GRa']+df['GRe']+df['GInd']+df['GOth']+df['GRef']+df['GSoc']




df[['Reg','InclRati']].groupby(['Reg','InclRati'],as_index=False).sum().plot(x='Reg',y='InclRati',rot=45, figsize=(10,4))



regions=list(df.Reg.unique())
plt.figure(figsize=(11, 6))

p3=plt.bar(regions,df[['Reg','SsrDrugs']].groupby(['Reg']).size()+df[['Reg','Terr']].groupby(['Reg']).size()+df[['Reg','Cor']].groupby(['Reg']).size(),color='magenta',edgecolor='black')
p1=plt.bar(regions,df[['Reg','SsrDrugs']].groupby(['Reg']).size()+df[['Reg','Terr']].groupby(['Reg']).size(),color='cyan',edgecolor='black')
p2=plt.bar(regions,df[['Reg','SsrDrugs']].groupby(['Reg']).size(),color='blue',edgecolor='black')
plt.xticks(rotation=90)
plt.legend(labels=['Corruption','Terrorism','Drugs'])
plt.show()


df.groupby('Reg').size().sort_values().plot(kind='bar')

df.groupby('Con').size().sort_values().tail(10).plot(kind='bar',rot=45)

