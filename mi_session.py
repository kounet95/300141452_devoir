def build_list():
    cont = int(input("Ajouter un autre etudiant ? (1/0) "))
    while cont != 0:
        nom = str(input("entre un nom:"))
        age = int(input("entre lage:"))
        print("nom:", " ", nom,"\n", "Age:",age)
        cont = int(input("Ajouter un autre etudiant ? (1/0) "))
build_list()  