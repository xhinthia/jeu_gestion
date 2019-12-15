import random
import os
import sys
from fonctions import *

a=1
while a==1:
	bandeau_clean("MENU PRINCIPAL")
	print ("<><><><><><><><><><><><><><><>")
	print (" ")
	print ("1 > Expédition")
	print ("")
	print ("2 > Quartier royal")
	print ("")
	print ("3 > Quartier marchand")
	print ("")
	print ("0 > Quitter")
	print (" ")
	print ("<><><><><><><><><><><><><><><>")
	choix=input()
	if str(choix)=="0":
		quit()
	elif str(choix)=="1":
		b=1
		while b==1:
			bandeau_clean("EXPEDITION")
			print ("<><><><><><><><><><><><><><><>")
			print ("")
			print ("1 > Combat") #action de combattre > choisis une troupe parmi les 3 > combat auto
			print ("")
			print ("2 > Minage") #action de miner : dure X secondes et toutes les 2s ou 3s pop-up
			print ("")
			print ("3 > Entraînement") #Utilise de l'or pour soit découvrir un nouveau type de mob soit up les présents
			print ("")
			print ("0 > Retour")
			print ("")
			print ("<><><><><><><><><><><><><><><>")
			choix=input()
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				combat()
			elif str(choix)=="2":
				minage()
			elif str(choix)=="3":
				entrainement()
			else:
				pass
	elif str(choix)=="2":
		b=1
		while b==1:
			bandeau_clean("QUARTIER ROYAL")
			print ("<><><><><><><><><><><><><><><>")
			print ("")
			print ("1 > Hall de guerre") # Consulter les troupes, carac, comp, lvl
			print ("")
			print ("2 > Salle des archives") #consulter les ennemis (déjà croisé ?)
			print ("")
			print ("3 > Eglise") #consulter les livres sacrés (artefacts)
			print ("")
			print ("0 > Retour")
			print ("")
			print ("<><><><><><><><><><><><><><><>")
			choix=input()
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				hall_guerre()
			elif str(choix)=="2":
				salle_archive()
			elif str(choix)=="3":
				eglise()
			else:
				pass
	elif str(choix)=="3":
		b=1
		while b==1:
			bandeau_clean("QUARTIER MARCHAND")
			print ("<><><><><><><><><><><><><><><>")
			print ("")
			print ("1 > Forgeron") #amélioration equipement
			print ("")
			print ("2 > Charpentier") #amélioration batiment contre minerais + or
			print ("")
			print ("3 > Marché noir") #amélioration générale du jeu
			print ("")
			print ("0 > Retour")
			print ("")
			print ("<><><><><><><><><><><><><><><>")
			choix=input()
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				forgeron()
			elif str(choix)=="2":
				charpentier()
			elif str(choix)=="3":
				marché_noir()
			else:
				pass
	else:
		pass

