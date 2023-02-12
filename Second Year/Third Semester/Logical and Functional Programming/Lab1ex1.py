class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None


class Lista:
    def __init__(self):
        self.prim = None


'''
crearea unei liste din valori citite pana la 0
'''


def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista


def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod


'''
tiparirea elementelor unei liste
'''


def tipar(lista):
    tipar_rec(lista.prim)


def tipar_rec(nod):
    if nod != None:
        print(nod.e)
        tipar_rec(nod.urm)


'''
program pentru test
'''


def transform(node):
    if node == None:
        return []
    else:
        x = node.e
        if x not in transform(node.urm):
            return [x] + transform(node.urm)
        return transform(node.urm)

def union(node1, node2):
    if node1 == None and node2 == None:
        return []
    if node2 == None and node1 != None:
        x = node1.e
        if x not in union(node1.urm, node2):
            return [x] + union(node1.urm, node2)
        return union(node1.urm, node2)
    if node1 == None and node2 != None:
        x = node2.e
        if x not in union(node1, node2.urm):
            return [x] + union(node1, node2.urm)
        return union(node1, node2.urm)
    if node1 != None and node2 != None:
        x = node1.e
        y = node2.e
        if x not in union(node1.urm, node2.urm) and y not in union(node1, node2.urm):
            if x != y:
                return [x] + [y] + union(node1.urm, node2.urm)
            return [x] + union(node1.urm, node2.urm)
        if x not in union(node1.urm, node2.urm):
            return [x] + union(node1.urm, node2.urm)
        if y not in union(node1.urm, node2.urm):
            return [y] + union(node1.urm, node2.urm)

def main():
    list = creareLista()
    s = transform(list.prim)
    print('The set is: ', s)
    a = creareLista()
    b = creareLista()
    s = union(a.prim, b.prim)
    print('The union set is: ', s)



main()

