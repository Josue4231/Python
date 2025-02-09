"""nb=int(input("Entrer un nombre entier"))
if nb>0 :
    print(f"{nb} est positif")
elif nb<0 :
    print(f"{nb} est négatif")
elif nb==0 :
    print(f"{nb} est nul")
else : 
    print(f"{nb} est un nombre qui existe pas ")
    """
"""age=int(input("Entrer votre age"))
if age<12 :
    print(f"A {age} ans , vous etes un enfant")
elif 12<age<18 :
    print(f"A {age} ans , vous etes un adolescent")
elif age>18 :
    print(f"A {age} ans , vous etes un aldulte")
else : 
    print("impossible de determiner votre age" )
    """

"""pdf=int(input("Entrer votre prix de fabrication"))
pdv=int(input("Entrer votre prix de vente"))
if pdf>pdv :
    print("perte")
elif pdv>pdf :
    print("profit")
else :
    print("inpossible")


pdf=float(input("Entrer votre prix de fabrication"))
pdv=float(input("Entrer votre prix de vente"))
if pdf>pdv :
    print("perte")
elif pdv>pdf :
    print("profit")
else :
    print("inpossible")
    """

cit=int(input("Entrer votre prix de location de citadine"))
berl=int(input("Entrer votre prix de location berline"))
sport=int(input("Entrer votre prix de location sportive"))
ess=float(input("Entrer votre prix de carburant en klm en essence"))
die=float(input("Entrer votre prix de carburant en klm en diesel"))

if cit<berl :
    print("Type de véhicule : Ciatdine")
else : 
    print("Le type de véhicule : Berline")
if ess>die :
    print("Carburant : Diesel")
else :
    print("Carburant : Essence")
if cit==80 :
    print("Durée de la location est de : 3") 
elif cit<80 :
    print("Durée de location est moin de : 3 jours")
else : 
    print("Durée de location est plus de : 3 jours")
if die<ess :
    print("Distance en km : 256")
elif die==ess :
    print("Distance  en km est moin de  : 256")
if cit<sport and sport>berl :
    print("fre commerciale : True") 
else :
    print("fre commerciale : False")
if cit<berl and cit<sport and die<ess : 
    print("le prix total de la location est de 681.4559999999999 euros.")
else : 
    print("le prix total de la location est superieur 681.4559999999999 euros.")



