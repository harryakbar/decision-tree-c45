from collections import OrderedDict


def deldup(li):
    """ Menghapus duplikasi dari list li 
        dan mengembalikan list baru dengan nilai yang unik
    """
    return list(OrderedDict.fromkeys(li))


def is_mono(t):
    """ Mengembalikan nilai True jika semua nilai t sama,
        selain itu mengembalikan False
    """
    for i in t:
        if i != t[0]:
            return False
    return True


def get_indexes(table, col, v):
    """ Mengembalikan index dari value v di kolom col
        pada table
    """
    li = []
    start = 0
    for row in table[col]:
        if row == v:
            index = table[col].index(row, start)
            li.append(index)
            start = index + 1
    return li


def get_values(t, col, indexes):
    """ Mengembalikan nilai pada index di kolom col pada tabel t """
    return [t[col][i] for i in range(len(t[col])) if i in indexes]


def del_values(t, ind):
    """ Membuat table baru dengan nilai ind """
    return {k: [v[i] for i in range(len(v)) if i in ind] for k, v in t.items()}


def get_subtables(t, col):
    """ Mengembalikan subtable dari tabel t yang dibagi oleh nilai pada kolom col """
    return [del_values(t, get_indexes(t, col, v)) for v in deldup(t[col])]
