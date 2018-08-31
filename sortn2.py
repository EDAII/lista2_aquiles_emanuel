import numpy as np
#import matplotlib.pyplot as plt
import random

def bubble_sort(v):
    for i in range(len(v)):
        for j in range(i+1 ,len(v)):
            if (v[j] < v[i]):
                aux = v[i]
                v[i] = v[j]
                v[j] = aux

def insertion_sort( lista ):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave


def selection_sort(v):
    v_original = v
    for i in range(len(v)):
        #plt.scatter(v_original, v)
        #plt.show()
        #plt.cln()
        swap = i + np.argmin(v[i:])
        (v[i], v[swap]) = (v[swap], v[i])  # troca a ordem dos valores da lista
    return v


v = range(21)  # uma lista de 0 a 20
v = np.array(v)
random.shuffle(v)
print(v)
op = int(input("escoha 1 para selection sort, 2 para insertion sort e 3 para bubble sort \n"))

if (op == 1):
    v_sort = selection_sort(v)
elif(op == 2):
    v_sort = insertion_sort(v)
elif(op == 3):
    v_sort = bubble_sort(v)

print(v)


