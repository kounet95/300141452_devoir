import os

def listingdirectory(directory):
    filelist = []
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        if os.path.isfile(entry_path):
            file_name, ext = os.path.splitext(entry)
            #CONVERTION EN MO 
            size = os.path.getsize(entry_path) / (1024 * 1024)
            
            filelist.append((file_name, ext, size))
    return filelist

#Tri par sélection selon la taille des fichiers
def tri2sélection(filelist):
    n = len(filelist)
    for i in range(n):
        #Selectionner un point de depart
        minindex = i
        for j in range(i + 1, n):
            if filelist[j][2] < filelist[minindex][2]:
                minindex = j
        filelist[i], filelist[minindex] = filelist[minindex], filelist[i]
    return filelist
#Tri à bulles selon le nom des fichiers
def tri2bulle(filelist):
    tail = len(filelist)
    for i in range(tail):
        #pour jusqua la fin du fichier 
        for j in range(0, tail - i - 1):
            if filelist[j][0] > filelist[j + 1][0]:
                filelist[j], filelist[j + 1] = filelist[j + 1], filelist[j]
    return filelist
#test les fonction des fonctions
chemin = '/Users/Utilisateur/OneDrive - Université Laval/Documents'
files = listingdirectory(chemin)
print("Fichiers dans le répertoire :", files)

chemin = tri2sélection(files.copy())
print("Fichiers triés par taille :", chemin)

vtri2bulle = tri2bulle(files.copy())
print("Fichiers triés par nom :", vtri2bulle)