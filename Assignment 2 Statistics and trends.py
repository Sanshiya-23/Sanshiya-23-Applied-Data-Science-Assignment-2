import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def readdf(name):
    df=pd.read_excel(name)
    df=df.fillna(0)
    # df.iloc[2,4:]=str(df.iloc[2,4:])
    df.columns=df.iloc[2,:]
    df=df.iloc[3:,:]
    df.columns=df.columns.map(str)
    l1=list(df.columns)
    l2=list()
    for i in l1:
        if '.0' in i:
            i=i.replace('.0','')
        l2.append(i)
    df.columns=l2
    print(df.columns)
    return df

def bar(df):
    df=df[df['Indicator Name']=='Agricultural land (% of land area)']
    plt.hist(df['2020'], bins=100)
    print(df['2020'])
    plt.xlabel('land area')
    plt.ylabel('Agricultural land')
    plt.title('Agricultural land (% of land area)')
    plt.describe()
    plt.show()

def heatmap(df):
    print(df)
    df = df[df['Indicator Name'] == 'Agricultural land (% of land area)']
    glue = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])#pivot('Country Name','2020')
    glue = glue.set_index('Country Name')
    print(glue)
    sns.heatmap(glue)
    plt.title('Agricultural irrigated land (% of total agricultural land))')
    plt.xlabel("year count")
    plt.describe()
    plt.show()

def heatmap1(df):
    print(df)
    df1=df
    df = df[df['Indicator Name'] == 'Agricultural land (% of land area)']
    #glue = df.drop(columns=['Country Name', 'Indicator Name', 'Indicator Code'])#pivot('Country Name','2020')
    glue=df.sort_values('2020', ascending=False)
    glue = glue[:10]
    li=list(glue['Country Code'])
    glue=glue[['Country Code','2000', '2005', '2010', '2015', '2020']]
    glue = glue.set_index('Country Code')
    print(glue)
    ax = plt.axes()
    sns.heatmap(glue, vmin=50, vmax=100)
    ax.set_title('Agriculture, forestry, and fishing, value added (% of GDP)')
    plt.show()

    df1 = df1[df1['Indicator Name'] == 'Agriculture, forestry, and fishing, value added (% of GDP)']
    print(li)
    df1=df1.loc[df1['Country Code'].isin(li)]
    glue1 = df1[['Country Code', '2000', '2005', '2010', '2015', '2020']]
    glue1 = glue1.set_index('Country Code')
    print(glue1)
    ax = plt.axes()
    sns.heatmap(glue1, cmap="crest")
    ax.set_title('Agricultural land (% of land area)')
    plt.show()
    plt.describe()
    return li

def combar(df,li):
    print(set(df['Indicator Name']))
    df = df.loc[df['Indicator Name'].isin([m for m in set(df['Indicator Name']) if "Agricult" in m])]
    #df = df[df['Indicator Name'] == 'Agricultural land (% of land area)']
    df = df.loc[df['Country Code'].isin(li)]
    #str=li[0]
    df=df[['Indicator Name','1970','1980', '1990', '2000', '2020']]
    df=df.set_index('Indicator Name')
    print(df)
    df.plot(kind="bar", figsize=(15, 8))

    plt.title("agricultural detail of top 10 country in Agricultural land (% of land area)")

    plt.xlabel("Indicator Name")

    plt.ylabel("year count")
    plt.describe()
    plt.show()

df=readdf('API_19_DS2_en_excel_v2_5351881.xls')
bar(df)
heatmap(df)
li=heatmap1(df)
combar(df,li)