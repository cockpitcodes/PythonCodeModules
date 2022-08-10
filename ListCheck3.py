"""There Is List A, List B.
Now Merge The 2 Into A New List Without Having A Dupplicate Element In It"""

lista=[1,2,3,4,5]
listb=[5,6,8,9,7,10,1,5]
listc=[]
lista.extend(listb)
lin_lista=len(lista)
print(lista)
for element in range(lin_lista):
    if (lista[element] not in listc):
        listc.append(lista[element])
print(listc)