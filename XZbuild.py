import random
import os
import sys
from fonctions import *

a=1
while a==1:
	choix=menu_3_choix("MENU PRINCIPAL","Expédition","Grand place","Quartier marchand","Quitter")
	if str(choix)=="0":
		quit()
	elif str(choix)=="1":
		b=1
		while b==1:
			choix=menu_3_choix("EXPEDITION","Combat","Minage","Entraînement","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("COMBAT","Combattre","Sélectionner un groupe","Composition des groupes","Retour")
			elif str(choix)=="2":
				choix=menu_3_choix("MINAGE","Miner","Améliorer mine","Améliorer équipement")
			elif str(choix)=="3":
				choix=menu_3_choix("ENTRAINEMENT","Financer","")
			else:
				pass
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_3_choix("GRAND PLACE","Hall de guerre","Salle des archives","Eglise","Retour")
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
			choix=menu_3_choix("QUARTIER MARCHAND","Forgeron","Charpentier","Marché noir","Retour")
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

