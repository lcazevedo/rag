from binarytree import Tree
from datetime import datetime

bst = Tree()

for i in range (100000):
    bst.inserir(i)

start = datetime.now()
a = bst.buscar(100)
print(f"{datetime.now() - start } para achar o 10")

start = datetime.now()
a = bst.buscar(90000)
print(f"{datetime.now() - start } para achar o 9000")

