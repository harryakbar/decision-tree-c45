import pandas as pd
import numpy as np
import json
from c45 import *

def classify(dframe):
    pop = dframe['popularity']
    ls = []
    for i in range(0,len(pop)):
        v = pop[i]
        if v < 45:
            ls.append('Unpopular')
        elif v >= 45 and v < 90:
            ls.append('Moderate')
        elif v >= 90 and v < 135:
            ls.append('Popular')
        elif v >= 135:
            ls.append('Very Popular')
    dframe['popularity'] = ls
    return dframe

def fixDf(dframe):
    genre = dframe['genres']
    company = dframe['production_companies']
    ls = []

    dframe = dframe.drop("homepage",1)
    dframe = dframe.drop("id",1)
    dframe = dframe.drop("keywords",1)
    dframe = dframe.drop("original_language",1)
    dframe = dframe.drop("original_title",1)
    dframe = dframe.drop("overview",1)
    dframe = dframe.drop("production_countries",1)
    dframe = dframe.drop("release_date",1)
    dframe = dframe.drop("spoken_languages",1)
    dframe = dframe.drop("status",1)
    dframe = dframe.drop("tagline",1)
    dframe = dframe.drop("title",1)

    for i in genre:
        v = json.loads(i)
        if len(v) != 0:
            ls.append(v[0].get('name'))
        else:
            ls.append('None')

    dframe['genres'] = ls

    ls = []
    for i in company:
        v = json.loads(i)
        if len(v) != 0:
            ls.append(v[0].get('name'))
        else:
            ls.append('None')

    dframe['production_companies'] = ls

    return dframe

if __name__ == '__main__':
    df = pd.read_csv('movies.csv')
    df = classify(df)
    df = fixDf(df)
    ls = df.to_dict('list')
    
    print(ls.keys())
    # for i in ls.keys():
    #     if i != 'popularity_category':
    #         print("{0} : {1}".format(i, gain(ls,i,'popularity_category')))
    print(df['popularity'])
