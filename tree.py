from utils import *
from c45 import *

def c45_tree(table, target):
    gains = []
    for key in table.keys():
        if key != target:
            gains.append((key, gain(table,key,target)))
    col = max(gains)[0]
    
    tree = []
    subtable = get_subtables(table,col)
    for t in subtable:
        v = t[col][0]
        if is_mono(t[target]):
            tree.append(['%s=%s' % (col, v), '%s=%s' % (target, t[target][0])])
        else:
            del t[col]
            tree.append(['%s=%s' % (col, v)] + c45_tree(t, target))
    return tree


    
    

