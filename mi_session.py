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
build_list()