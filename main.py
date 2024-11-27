from random import *
from pyscript import document

# LISTE D'EXCUSES :
Liste_Sujet = [["Mon devoir a été", "Le devoir a été"],
["Un sorcier", "Un chat", "Un vent", "Talmo", "Un neuille", "Midas", "Jean Fils", "Le Freestyle du million", "Fresh la douille", "Monsieur Alves", "Un robot", "Un tapis", "Un groupe de tortues Ninja", "Un PDG de Brawl Star", "Colonel Médor", "Mohamed Henni", "Un main Kit", "Un raciste", "Squeak le sigma", "Le fou du bus", "Un groupe de terroristes", "Un doberman", "Un type", "L’opinel 13",  "Le bambi", "Le lutteur russe","Un yop à la fraise", "Un coca zombi", "TheKairi78", "Un gang de Brooklyn", "N’golo Kanté", "Raoul le mec chill", "Le cratère du Ngorongoro", "Topi taupe", "Roi boo", "Le triple monstre", "Glhynnyl Hylhyr Yzzyghy",  "Oussama Amar", "Pamplemousse Namaspamouss", "Le wesh wesh du 69 la trik pelo", "Bassem", "Allo selem 🐵🙈", "SpiderManUn", "Un gateau BN",  "Dj octave sous dj prime", "Le J c’est le S", "Jul", "Le lapin de nesquik", "Un crachat de Shrek", "El diablo", "Le trépied", "Un raclo", "Rebeudeter", "Squeezos", "Don Pollo", "Le petit filou qui traine dans mon frigo depuis 3 ans", "Pandicorn" ,"L'inspecteur gadjet", "Le crousti-fromage"],
["L'Hchouma",   "Une thérapie", "Une bande de raccoons", "Une créature de la nuit", "Ma boîte mail","La cagoule temu ", "Une chaussettes Nike", "La mentalité kaizen", "La grosse tana", "La go qui fait la go", "Une crêpe wahou", "La kiffance", "La mangue Oasis", "Ines 92i", "La nouvelle méta",],
["Les fruits Oasis", "Ramzo et Rapido", "Maxus, Leonard et Jérôme", "Des terroristes", "Les Tortues Ninja", "Les powers rangers", "Les gros Neuilles","Pytagore et Thales", "Les macaques", "Oggy et les cafards", "Zig et Sharko", "Les barbapapa", "Les lapins crétins"]]
Liste_Verbe = ["mangé", "emprunté", "transformé", "abducté", "englouti", "pris", "enlevé", "zouké", "batifolé", "zigzagué", "malaxé", "loufoqué", "vendu", "détruit", "peint", "cuisiné", "nettoyé", "emporté", "embauché", "licencié", "battu", "arrêté", "descendu", "volé", "tué", "coursé", "planté","Chillé", "Drifté", "Flambé", "Cassé", "Grillé", "Killé", "Kiqué", "Tapé", "Clashé", "Explosé", "Éclaté", "Tapé dans l’œil de", "Tabassé", "Chassé", "Dégagé", "Allumé", "Hacké", "Bousillé"]
Liste_Adjectif = [["en mode tranquilou Bilou", "en mode cool raoul", "en mode relax max", "sous frozen", "complétement zehef", "sous El Mordjene", "avec 2 de QI", "sous chantilly radioactive"],
 ["magique", "lugubre", "biscornu", "zombie", "macabre", "abracadabrantesque", "gargantuesque", "neuillesque"],
 ["déjanté", "complètement perdu", "complétement hurluberlu", "affamé", "farfelu", "bouillonnant", "zinzolin"]]

def Generateur(event):
  Excuse = []
  Type_Sujet = Liste_Sujet[randint(0, 3)]
  Type_Adjectif = Liste_Adjectif[randint(0, 2)]
  Sujet_Exc = Type_Sujet[randint(0, len(Type_Sujet)-1)]
  Verbe_Exc = Liste_Verbe[randint(0, len(Liste_Verbe)-1)].lower()
  Adjectif_Sujet = (Type_Adjectif[randint(0, len(Type_Adjectif)-1)])
  Excuse.append(Sujet_Exc)

  # Si le sujet est "devoir"
  if Type_Sujet == Liste_Sujet[0]:
    Excuse.append(Verbe_Exc)
    Excuse.append("par")
    Complement_Exc = Liste_Sujet[randint(1,3)]
    Complement_Exc = Complement_Exc[randint(0, len(Complement_Exc)-1)]
    Excuse.append(Complement_Exc)

  #Reste
  else:
    # Si le sujet est au pluriel
    if Type_Sujet == Liste_Sujet[3]:
      if randint(1,2) == 1:
        if Type_Adjectif == Liste_Adjectif[1] or Type_Adjectif == Liste_Adjectif[2]:
          Adjectif_Sujet += "s"
        Excuse.append(Adjectif_Sujet)
      Excuse.append("ont")

    # Si le sujet est au feminin
    elif Type_Sujet == Liste_Sujet[2]:
      if randint(1,2) == 1:
        if Type_Adjectif == Liste_Adjectif[1]:
          Adjectif_Sujet += "s" 
        elif Type_Adjectif == Liste_Adjectif[2]:
          Adjectif_Sujet += "es"
        Excuse.append(Adjectif_Sujet)
      Excuse.append("a")

    # Si le sujet est au masculin
    elif Type_Sujet == Liste_Sujet[1]:
      if randint(1,2) == 1:
        Excuse.append(Adjectif_Sujet)
      Excuse.append("a")

    # Ajout du verbe et "mon devoir"
    Excuse.append(Verbe_Exc)
    Excuse.append("mon devoir")

  # TRANSFORMATION DE LA LIST EN STRING
  Excuse = " ".join(Excuse)
  Excuse = Excuse + "."
  output_div = document.querySelector("#output")
  output_div.innerText = Excuse
