import os, time
os.system("cls")

#listes pour animations
soleil_lever= ["soleil(1).txt","soleil(2).txt","soleil(3).txt","soleil(4).txt","bonmatin.txt" ]
soleil_coucher= ["bonnenuit.txt", "soleil(4).txt","soleil(3).txt","soleil(2).txt","soleil(1).txt" ]
horloge= ['horloge(1).txt','horloge(2).txt','horloge(3).txt']
frames_lever= []
frames_coucher= []
frames_horloge= []

#fonction animation
def animation_ascii(ascii, frames_list):
    for name in ascii:
        with open(name, "r", encoding= "utf8") as f:
            frames_list.append(f.readlines())

    for frame in frames_list:
        os.system('cls')
        print("".join(frame))
        time.sleep(.8)


animation_ascii(soleil_lever, frames_lever)
os.system('cls')
time.sleep(1)
animation_ascii(horloge, frames_horloge)
os.system('cls')
time.sleep(1)
animation_ascii(soleil_coucher, frames_coucher)



