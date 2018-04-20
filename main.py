import pandas as pd
import numpy as np
import json
from tree import *
from c45 import *
import json

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

    ls = []
    mean = dframe['vote_average'].mean()
    for i in dframe['vote_average']:
        if i >= mean:
            ls.append("%s>" % (mean))
        else:
            ls.append("%s<" % (mean))
    
    dframe['vote_average'] = ls

    ls = []
    mean = dframe['runtime'].mean()
    for i in dframe['runtime']:
        if i >= mean:
            ls.append("%s>" % (mean))
        else:
            ls.append("%s<" % (mean))

    dframe['runtime'] = ls

    ls = []
    mean = dframe['vote_count'].mean()
    for i in dframe['vote_count']:
        if i >= mean:
            ls.append("%s>" % (mean))
        else:
            ls.append("%s<" % (mean))

    dframe['vote_count'] = ls

    ls = []
    mean = dframe['revenue'].mean()
    for i in dframe['revenue']:
        if i >= mean:
            ls.append("%s>" % (mean))
        else:
            ls.append("%s<" % (mean))

    dframe['revenue'] = ls

    ls = []
    mean = dframe['budget'].mean()
    for i in dframe['budget']:
        if i >= mean:
            ls.append("%s>" % (mean))
        else:
            ls.append("%s<" % (mean))

    dframe['budget'] = ls

    return dframe
    
def listUrutan(table, target):
    dic = {}
    for key in table.keys():
        if key != target:
            dic[key] = gain(table, key, target)
    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    return sorted_dic

def test_data(tree, data_input):
    for t in tree:
        if (t in data_input):
            if (len(tree[t]) > 1 and type(tree[t]) != str):
                data_input = data_input[1:]
                test_data(tree[t], data_input)
            else:
                print(tree[t])

if __name__ == '__main__':
    df = pd.read_csv('movies.csv')
    df = classify(df).head(n=100)
    df = fixDf(df)
    ls = df.to_dict('list')
    dct = listUrutan(ls,'popularity')
    data_input = ["production_companies=Columbia Pictures","runtime=127.4<", "genres=Action", "revenue=661092697.61<"]
    x = c45_tree(ls,'popularity')
    test_data(x, data_input)
    res = json.dumps(x, sort_keys=False, indent=4, separators=(',', ': '))
    # print(res)
