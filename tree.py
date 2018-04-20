from utils import *
from c45 import *

def c45_tree(table, target):
    
    if len(table)!= 1:
        col = max([(k, gain(table, k, target)) for k in table.keys() if k != target],
                key=lambda x: x[1])[0]
        
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
    else:
        return []

    
    

