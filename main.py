#Harry Potter Test

print(" Dies ist das Quiz der Hogwarts Häsuer. Der magische Hut, wird anhand deiner Entscheidungen, ein Haus für dich erwählen. _/-\_")
# quizhauptmatrix
print("\n")
score = 0

#Frage 1
answer1 = input("Es geht los! Dir wird der magische Hut auf den Kopf gesetzt – Hmmm, was soll ich nur mit dir machen??? \na. Lass dir Zeit ;-) \nb. Ich kann ja in der Zwischenzeit ein Buch lesen. \nc. Nicht Slytherin, nicht Slytherin,... \nd. Ist doch klar! \nAntwort: ")
if answer1 == "b" or answer1 == "Ich kann ja in der Zwischenzeit ein Buch lesen.":
    score += 1
    print("Du scheinst mir ja ein ganz schlauer zu sein!")
    print("Wert des Schülers:", score)
    print("\n") #Leerzeile
else: print("Hahah... Ich glaube deine Eltern sind Muggel.")
print("Wert des Schülers:",score)
print("\n")  #Leerzeile

#Frage 2
answer1 = input("Welche der folgenden Eigenschaften ist dir besonders wichtig? \na. Ruhm \nb. Treue \nc. Mut \nd. Weisheit \nAntwort: ")
if answer1 == "c" or answer1 == "Mut":
    score += 1
    print("Aus dir kann mal ein richtiger Zauberer werden.")
    print("Wert des Schülers:", score)
    print("\n") #Leerzeile
else: print("Naja ein echter Gryffindor wirst du bestimmt nicht. ")
print("Wert des Schülers:",score)
print("\n")  #Leerzeile

#Frage 3
answer1 = input("Welche magische Kraft hättest du am liebsten? \na. Parselmund \nb. Gedankenlesen \nc. Unsichtbarkeit \nd. Verwandlung \nAntwort: ")
if answer1 == "a" or answer1 == "Parselmund":
    score += 1
    print("Da hat wohl jemand schon die Künste der dunklen Magie kennengelernt.")
    print("Wert des Schülers:", score)
    print("\n") #Leerzeile
else: print("Noch nicht einmal eine Stunde in diesem Haus und schon an Schabernack denken. Scheeren Sie sich fort. ")
print("Wert des Schülers:",score)
print("\n")  #Leerzeile

#Frage 4
answer1 = input("Welches Haustier hast du junger Freund in diese heiligen Hallen gebracht?  \na. Ich hasse Tiere. \nb. Ein Kröte macht nicht viel Arbeit. \nc. Eine graue Ratte. \nd. Eine Schleiereule. \nAntwort: ")
if answer1 == "d" or answer1 == "Eine Schleiereule.":
    score += 1
    print("Gute Wahl! Passen Sie aber auf das Gefieder auf, denn sonst landet der Vogel in der Küche. ")
    print("Wert des Schülers:", score)
    print("\n") #Leerzeile
else: print("Oh schrecklich! Sind Sie zufällig mit den rothaarigen Unglückswesen der Weasleys verwandt.")
print("Wert des Schülers:",score)
print("\n")  #Leerzeile


#ergbenismatrize
if score <= 1:
    print("Naja mit Zaubern sieht es bei Ihnen schlecht aus. Versuchen Sie trotzdem ihr bestes in Hufflepuff.")
    print("Dein gesamt Wert als Schüler beträgt:", score, ".")
elif score == 2:
    print("Fast wäre es ein Slytherin geworden, leider sehe ich da doch ein wenig Muggelblut. Du schläfst ab sofort im Schlafsaal der Ravenclaw.")
    print("Dein gesamt Wert als Schüler beträgt:", score, ".")

elif score == 3:
    print("Es ist eindeutig! Schon an der Spitze ihres Zauberstabes kann ich das ablesen. Ein neuer Slytherin! ") #etwas zweideutig ik aber mir ist nichts besseres eingefallen :-/
    print("Dein gesamt Wert als Schüler beträgt:", score, ".")
else:
    print("Ich sehe das potential eines neuen Potters. Fantastisch. Sie sind ein echter Gryffindor! " )
    print("Dein gesamt Wert als Schüler beträgt:", score, ".")


print("Nun ist es Zeit deinen Koffer zu schnappen und deine neue Schule zu erkunden. ")

