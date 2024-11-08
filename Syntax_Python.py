### 2- Définition de la fonction pour afficher le message de bienvenue

def bienvenue():
    print("Bienvenue chez Python Pizza Livraisons !")
# Appel de la fonction
bienvenue()

### 3- Fonction "input" et stockage de variable "size"

# Demander à l'utilisateur la taille de la pizza
size = input("Quelle taille de pizza souhaitez-vous ? (Petite, Moyenne, Grande) : ")
# Afficher la taille choisie
print(f"Vous avez choisi une pizza de taille : {size}")

### 4- Fonction "input" et stockage de variable "add_pepperoni"

# Demander à l'utilisateur s'il souhaite ajouter du pepperoni
add_pepperoni = input("Souhaitez-vous ajouter du pepperoni à votre pizza ? (oui/non) : ")
# Afficher la réponse de l'utilisateur
print(f"Vous avez choisi d'ajouter du pepperoni : {add_pepperoni}")

### 5- Fonction "input" et stockage de variable "extra_cheese"

# Demande à l'utilisateur s'il souhaite du fromage supplémentaire
extra_cheese = input("Souhaitez-vous du fromage supplémentaire ? (oui/non) : ")
# Affichage de la réponse
if extra_cheese.lower() == 'oui':
    print("Vous avez choisi d'ajouter du fromage supplémentaire.")
else:
    print("Vous avez choisi de ne pas ajouter de fromage supplémentaire.")