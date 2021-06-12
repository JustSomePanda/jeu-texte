import os, time
os.system("cls")

#listes pour animations
soleil_lever= ["soleil(1).txt","soleil(2).txt","soleil(3).txt","soleil(4).txt","bonmatin.txt" ]
soleil_coucher= ["bonnenuit.txt", "soleil(4).txt","soleil(3).txt","soleil(2).txt","soleil(1).txt" ]
horloge= ['travailler.txt', 'horloge(1).txt','horloge(2).txt','horloge(3).txt']
frames_lever= []
frames_coucher= []
frames_horloge= []

#fonction animation
def animation_ascii(ascii, frames_list, temps):      #ascii = liste des images     frames_list = liste vide     temps =  temps entre images
    for name in ascii:     #boucle qui ouvre fichier avec image et met chaque image dans le liste vide
        with open(name, "r", encoding= "utf8") as f:
            frames_list.append(f.readlines())

    for frame in frames_list:       # boucle qui efface l'écran après chaque image et crée l'animation
        os.system('cls')
        print("".join(frame))
        time.sleep(temps)      #temps entre chaque image


#listes pour jeu

liste_enonce = ["Bonjour! Voulez-vous reveiller?", "Allez-vous habiller?", "Quel est votre choix de transport?", "Vous avez finalement terminé! \n Voila tes collegues! Voulez-vous prendre un café avec eux?", "Où est-ce que tu veux acheter ton café?", "Maintenant, vous devez aller à la maison. \nQuel est votre choix de transport?", "Qu'allez-vous faire pour le souper?", "Voulez-vous regarder de la télévision?"]
liste_options = [ 
    ["1. Reveiller", "2. Dormir"],   
    ["1. Rester en pyjama", "2. S'habiller pour sortir dehors"],
    ["1. Marcher", "2. Faire du velo", "3. Prendre le bus"],
    ["1. Oui! Ce serait du fun!", "2. Non... vous êtes trop fatigué..."],
    ["1. Tim Hortons", "2. Starbucks"],
    ["1. Marcher", "2. Faire du velo", "3. Prendre le bus"],
    ["1. Cuisiner", "2. Acheter de la pizza"],
    ["1. Oui! Il faut quand même terminer le film que vous avez commencé hier soir!", "2. Non. Vous devez vous lever top demain!"]
]
liste_reponses = [
    ["Vous sortez de votre lit pour commencer la journee!", "Vous allez dormir... Au revoir!"],
    ["Etes-vous sur de rester en pyjama?", "Vous etes maintenant pret pour travailler!"],
    ["Ah zut.. vous etes en retard...", "Vous etes a temps! Ouf.. c'etait faitguant..", "Oups, vous etes arrivez trop tot!"],
    ["Vous quittez avec vos camarades :)", "Vous allez à la maison après une longue journée de travail! :)"],
    ["Miam, un boston cream avec un petit café glace!", "Miam, un frappucino caramel!"],
    ["Ah, qu'il fait beau dehors!", "Ouf, le vélo est toujours faitguant! Mais ça aide à rester en forme!", "Ah non! L'autobus est tombé en panne!"],
    ["Oooooh, c'est un bon plat saine!", "Woaaaa, la pizza!!!"],
    ["Ah non! Je n'ai pas payé attention a l'heure! Je vais le regretter demain...", "Bonne nuit, madame la narratrice!"]
]


#fonction enonce
def enonce(texte, options):
    print(texte)
    time.sleep(1)
    print('\n'.join(options))


#fontion choix et resultats
def choix_utilisateurs(rangee):
    while True:

        option_utilisateur = int(input())
        nombre_option = len(liste_options[rangee])
        
        #repete la reponse
        while option_utilisateur < 1 or option_utilisateur > nombre_option:
                print("Ceci n'est pas une réponse valide...")
                time.sleep(0.5)
                option_utilisateur = int(input("Veuillez repeter votre reponse: "))

        #si option est valide, resultat sera un option du liste 
        
        resultat= liste_reponses[rangee][option_utilisateur -1] #rangee est 0 au début du boucle .... option utilisateur est la colone dans le liste 2d (l'utilisateur choisi ceci)
        time.sleep(1)
        print(resultat)
        rangee += 1 #on ajoute 1 à rangée le plus que le jeu s'avance
           

        #si option est "Dormir", le jeu se termine et il y a une animation
        if resultat == liste_reponses[0][1]:
            animation_ascii(soleil_coucher, frames_coucher, .7)
            break
        
        #si option est "rester en pyjama" le jeu demnde si tu es sûr. Si oui, tu dors, si non, tu t'habille
        if resultat == liste_reponses[1][0]:
            x= input("o ou n: \n")
            while x != "o" or x!= "n":
                if x== "o": 
                        resultat = liste_reponses[0][1]
                        print(resultat)
                        time.sleep(1)
                        animation_ascii(soleil_coucher, frames_coucher, .7)
                        break

                elif x== "n":
                    resultat = liste_reponses[1][1]
                    print(resultat)
                    break
                
                
                else:
                        print("Ceci n'est pas une réponse valide...")
                        time.sleep(0.5)
                        x = input("Veuillez repeter votre reponse: ")

    

        #lorsque tu vas au travail, n'importe quel option que tu choisi montrera une animtation
        #Option 3 ne fontionne pas.... idk why
        if resultat == liste_reponses[2][0] or resultat == liste_reponses[2][1] or resultat == liste_reponses[2][2]:
            time.sleep(2)
            animation_ascii(horloge, frames_horloge, 2)

        #si vous ne partez pas avec vos camarades, vous allez directement a la maison
        if rangee == 4 and option_utilisateur== 2:
            rangee +=1

        enonce(liste_enonce[rangee], liste_options[rangee])
        #        #Même si il n'y a plus d'énoncé, la boucle continue. Toutefois, ceci cause une erreur car l'index des listes n'éxiste pas. Pour éviter ceci, on a un try except
        if resultat == liste_reponses[7]:
            print("Vous allez maintenant vous coucher!")
            break



        
        

def main():  
    #animation_ascii(soleil_lever, frames_lever, .7)

    #jeu
    continuer = 'o'
    while continuer == 'o':
        enonce(liste_enonce[0], liste_options[0])  
        choix_utilisateurs(0)
        continuer = None
        while continuer != 'o' and continuer != 'n':
            continuer = input('Voulez-vous jouer encore? (o/n)? ')
        if continuer == 'o':

            print()
        elif continuer == 'n':
            time.sleep(.5)
            print("D'accoord :) Bonne journee")
            time.sleep(.5)

main()

