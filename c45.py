import math
import utils

def freq(table, col, v):
    return table[col].count(v)


def entropy(table, res_col):
    s = 0
    for v in utils.deldup(table[res_col]):
        p = freq(table, res_col, v) / float(len(table[res_col]))
        s += p * math.log(p, 2)
    return -s


def remainder(table, col, res_col):
    s = 0
    for subt in utils.get_subtables(table, col):
        s += (float(len(subt[col])) / len(table[col])) * entropy(subt, res_col)
    return s


def gain(table, x, res_col):
    return entropy(table, res_col) - remainder(table, x, res_col)
