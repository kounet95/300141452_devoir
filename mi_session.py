def build_list():
    cont = int(input("Ajouter un autre etudiant ? (1/0) "))
    li = []
    while cont != 0:
        nom = str(input("entre un nom:"))
        age = int(input("entre lage:"))
        print("nom:", " ", nom,"\n", "Age:",age)
        li.append((nom,age))
        cont = int(input("Ajouter un autre etudiant ? (1/0) "))
    return print(li)
def switch(liste,i,j):
    print(liste)
    c = liste[i]
    liste[i] = liste[j]
    liste[j] = c
    return print(liste)
 
def bubbleSort(li):
     while (True):
        permutation = 0
        print(li)
        for k in range(len(li)-1):
            if li[k]>li[k+1]:
                switch(li,k,k+1)
                permutation+=1
        if (permutation==0):
            return li
        
def selectionSort(l):
    while (True):
        permutation = 0
        print(l)
        min = l[0][1]
        for i in range(len(l)-1):
            if min > l[i][i+1]:
                min = l[i][i+1]
                switch(l,i,i+1)
                permutation+=1
        if (permutation==0):
            return l

lis = [("Viny", 34),("Ryan", 43),("Tity", 31),("Antony", 27),
       ("Calvin", 39),("Lilian", 27)] 
#mes appel de fonction pour test decocher le commentaire par fonction pour verifier
#selectionSort(lis)
bubbleSort(lis)      
switch(lis,1,2)
#build_list()