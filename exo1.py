#EXO1
#1)
etudiant={"Josue":10.5,"Jotaro":12.5,"Jordan":14.0}
#2)
print(etudiant["Josue"])
#3)
x=etudiant.keys()
print(x)
y=etudiant.values()
print(y)
#5)
etudiant["Jordan"]=12     
#6)
del etudiant["Jotaro"]
print(etudiant)
#7)
z=int(input("Entrer un nombre au hazard"))
etudiant["Jojo"]=z
print(etudiant)
#8)
meilleure_note = max(etudiant, key=etudiant.get)
print(f"L'étudiant avec la meilleure note est {meilleure_note} avec {etudiant[meilleure_note]}.")
#9)
etudiants= dict(etudiant)
print(etudiants)
#10)
m=float(input("Entrer une mutiplication"))
etudiant["Josue"]=10.5*m*100
etudiant["Jordan"]=13.5*m*100
etudiant["Jojo"]=15*m*100
print(etudiant)


