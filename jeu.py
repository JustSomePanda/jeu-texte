import os, time
os.system("cls")
os.system("color")

#listes pour animations
soleil_lever = ["soleil(1).txt","soleil(2).txt","soleil(3).txt","soleil(4).txt","bonmatin.txt" ]
soleil_coucher = ["bonnenuit.txt", "soleil(4).txt","soleil(3).txt","soleil(2).txt","soleil(1).txt" ]
horloge = ['travailler.txt', 'horloge(1).txt','horloge(2).txt','horloge(3).txt']
collegue = ['collegue.txt']
ville = ['ville.txt']
youtube= ["youtube.txt"]
patronne = ["boss.txt"]
frames_lever = []
frames_coucher = []
frames_horloge = []
liste_image = []

#listes pour jeu
liste_enonce = ["Bonjour! Voulez-vous vous réveiller?", "Allez-vous vous habiller?", "Quel est votre choix de transport?", "Qu'allez-vous faire entre temps?", "Vous avez finalement terminé! \nVoilà tes collègues! Voulez-vous prendre un café avec eux?", "Où est-ce que tu veux acheter ton café?", "Maintenant, vous devez aller à la maison. \nQuel est votre choix de transport?", "Qu'allez-vous faire maintenant?", "Qu'allez-vous faire pour le souper?", "Voulez-vous regarder de la télévision?"]

liste_options = [ 
    ["1. Réveiller", "2. Dormir"],   
    ["1. Rester en pyjama", "2. S'habiller pour sortir dehors"],
    ["1. Marcher", "2. Faire du vélo", "3. Prendre le bus"],
    ["1. Faire une marche dans la ville", "2. Visionner une video sur YouTube", "3. Discuter avec un collegue"],
    ["1. Oui! Ce serait du fun!", "2. Non... vous êtes trop fatigué..."],
    ["1. Tim Hortons", "2. Starbucks"],
    ["1. Marcher", "2. Faire du vélo", "3. Prendre le bus"],
    ["1. Marcher", "3. Faire du velo", "3. Prendre un taxi"],
    ["1. Cuisiner", "2. Acheter de la pizza"],
    ["1. Oui! Il faut quand même terminer le film que vous avez commencé hier soir!", "2. Non. Vous devez vous lever top demain!"]
]

liste_reponses = [
    ["Vous sortez de votre lit pour commencer la journée!", "Vous allez dormir... Au revoir!"],
    ["Êtes-vous sûr de rester en pyjama?", "Vous êtes maintenant prêt pour travailler!"],
    ["Ah zut.. vous êtes en retard...", "Vous êtes à temps! Ouf.. c'etait faitguant..", "Oups, vous êtes arrivez trop tot!"],
    ["Marcher, c'est agreable :)", "Hmmm quelle video...", "Mark est arrive tôt comme d'habitude"],
    ["Vous quittez avec vos camarades :)", "Vous allez à la maison après une longue journée de travail! :)"],
    ["Miam, un 'boston cream' avec un petit café glace!", "Miam, un frapuccino caramel!"],
    ["Ah, il fait beau dehors!", "Ouf, faire du vélo est toujours fatigant! Mais ça aide à rester en forme!", "Ah non! L'autobus est tombé en panne!"],
    ["Ah, il fait beau dehors!", "Ouf, faire du vélo est toujours fatigant! Mais ça aide à rester en forme!", "C'était bien cher ce voyage!"],
    ["Oooooh, c'est un bon plat saine!", "Woaaaa, la pizza!!!"],
    ["Ah non! Je n'ai pas payé attention à l'heure! Je vais le regretter demain...", "Bonne nuit, madame la narratrice!"]
]

#fonction animation
def animation_ascii(ascii, frames_list, temps):   
    for name in ascii:     
        with open(name, "r", encoding= "utf8") as f:
            frames_list.append(f.readlines())

    for frame in frames_list:       
        os.system("cls")
        print("".join(frame))
        time.sleep(temps)  


#fonctions discussions
def discussion_mark():
    animation_ascii(collegue, liste_image, 2)
    print("- Bonjour Mark! \n")
    time.sleep(2)
    print("\033[0;94;40m- Salut...\n")
    time.sleep(2)
    print("\033[0;0;40m- Ça va? Tu as l'aire triste.\n")
    time.sleep(2)
    print("\033[0;94;40m- Ouais... j'ai mal dormi hier soir et j'en ai pas envie d'être ici... \n- Tu sais ce qu'on va faire aujourd'hui?\n")
    time.sleep(2)
    print("\033[0;0;40m- Euh... Je crois qu'il va falloir qu'on organise tous les fichiers.\n")
    time.sleep(2)
    print("\033[0;94;40m- Ouch! Ça durera toute la journée!\n")
    time.sleep(2)
    print("\033[0;0;40m- Oh il est 9h. Hop, au travail maintenant!\n")


def discussion_patronne():
    animation_ascii(patronne, liste_image, 2)
    print("- Je m'excuse pour le retard, Madame la patronne!\n")
    time.sleep(2)
    print("\033[0;92;40m- Bonjour...!\n- Vous savez bien que ceci est irresponsable!\n ")
    time.sleep(2)
    print("\033[0;0;40m- Je vous assure que ceci n'arriverait plus!\n")
    time.sleep(2)
    print("\033[0;92;40m- D'accord... Bref, aujourd'hui j'aurais une rencontre. C'est-à-dire que toi et Mark, vous êtes responsable d'organiser les fichiers dans mon bureau.\n- Hop, au travail maintenant!")
    print("\033[0;0;40m- \n")


#fonction énonce
def enonce(texte, options):
    print(texte)
    time.sleep(1)
    print('\n'.join(options))


#fontion choix et resultats
def choix_utilisateurs(rangee):
    while True:
        option_utilisateur = int(input())
        nombre_option = len(liste_options[rangee])
        
        while option_utilisateur < 1 or option_utilisateur > nombre_option:
                print("Ceci n'est pas une réponse valide...")
                time.sleep(0.5)
                option_utilisateur = int(input("Veuillez repeter votre réponse: "))
        
        resultat= liste_reponses[rangee][option_utilisateur -1] 
        time.sleep(1)
        print(resultat)
        print()
        rangee += 1 
       
     
        if resultat == liste_reponses[1][0]:
            x= input("o ou n: \n")

            while x != "o" or x!= "n":

                if x== "o": 
                    resultat = liste_reponses[0][1]
                    print(resultat)
                    time.sleep(1)
                    resultat == liste_reponses[0][1]
                    break

                elif x== "n":
                    resultat = liste_reponses[1][1]
                    print(resultat)
                    break
                
                
                else:
                        print("Ceci n'est pas une réponse valide...")
                        time.sleep(0.5)
                        x = input("Veuillez repeter votre réponse: ")

        if resultat == liste_reponses[0][1]:    
            animation_ascii(soleil_coucher, frames_coucher, .7)
            break
        
        if resultat == liste_reponses[2][0]:
            time.sleep(3)
            discussion_patronne()
            time.sleep(3)
            animation_ascii(horloge, frames_horloge, 2)
            rangee += 1

        if resultat == liste_reponses[2][1]:
            time.sleep(2)
            animation_ascii(horloge, frames_horloge, 2)
            rangee += 1

        if resultat == liste_reponses[3][0]:
            animation_ascii(ville, liste_image, 2)
            print("Hop, au travail maintenant!")
            time.sleep(3)
            animation_ascii(horloge, frames_horloge, 2)
        
        if resultat == liste_reponses[3][1]:
            animation_ascii(youtube, liste_image, 2)
            print("Hop, au travail maintenant!")
            time.sleep(3)
            animation_ascii(horloge, frames_horloge, 2)

        if resultat == liste_reponses[3][2]:
            time.sleep(3)
            discussion_mark()
            time.sleep(3)
            animation_ascii(horloge, frames_horloge, 2)

        if rangee == 5 and option_utilisateur== 2:
            rangee +=1
        
        if resultat == liste_reponses[6][0] or resultat == liste_reponses[6][1]:
            rangee += 1

        try:
            enonce(liste_enonce[rangee], liste_options[rangee]) 
        
        except IndexError: 
            time.sleep(1.5)
            print("Vous allez maintenant vous coucher!")
            animation_ascii(soleil_coucher,frames_coucher, .7)
            break


#fonction principale
def main():  
    animation_ascii(soleil_lever, frames_lever, .7)
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
            print("D'accord :) Bonne journée")
            time.sleep(.5)

main()

