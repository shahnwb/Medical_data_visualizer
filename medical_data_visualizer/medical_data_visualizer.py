import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight'] / ((df['height']/100) * (df['height'] / 100))
df.loc[bmi > 25, 'overweight'] = 1
df.loc[bmi <= 25, 'overweight'] = 0

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars= ['cholesterol','gluc','smoke','alco','active','overweight'])



    # 6
    df_cat1 = df_cat.groupby('cardio').value_counts()
    print(df_cat1)
    

    # 7
    g = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')


    # 8
    fig = g


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df.drop(df.loc[(df['ap_lo'] > df['ap_hi'])].index, inplace = True)
    df.drop(df.loc[(df['height'] < df['height'].quantile(0.025))].index, inplace = True)
    df.drop(df.loc[(df['height'] > df['height'].quantile(0.975))].index, inplace = True)
    df.drop(df.loc[(df['weight']) < df['weight'].quantile(0.025)].index, inplace = True)
    df.drop(df.loc[(df['weight']) > df['weight'].quantile(0.975)].index, inplace = True)
    df_heat = df
    
    # 12
    corr = df.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    

    # 14
    fig, ax = plt.subplots()

    # 15
    g = sns.heatmap(corr, mask=mask, vmax = 1, vmin = -1, annot = True)


    # 16
    fig.savefig('heatmap.png')
    return fig
