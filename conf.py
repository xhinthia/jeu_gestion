import os
import sys
import random

"""	menu principal
		

		Melange
			Melange 1
				Consulter
				Modifier
			Melange 2
				Consulter
				Modifier
			Melange 3
				Consulter
				Modifier
		Particules élémentaires
			Alclains
			Alcalino-terreux
			Hallogènes
			Gaz inertes


			
"""
a=0
while a==0:
	os.system('clear')
	print (" ")
	print ("1 - Exploration")
	print ("2 - Entraînement")
	print ("0 - Quitter")
	print (" ")
	choix=input("choix : ")
	os.system('clear')
	if str(choix)=="1":
		print (" ")
		print ("1 - Combat")
		print ("2 - Artisanat")
		print ("3 - Build")
		print ("4 - Bestiaire")
		print ("5 - Epreuve")
		print ("0 - Retour")
		print (" ")
		choix=input("choix : ")
		os.system('clear')
		if str(choix)=="1":
			print ("1 - ")
		elif str(choix)=="2":
			print ("2 -  ")
		elif str(choix)=="3":
			print (" ")
		elif str(choix)=="4":
			print (" ")
			print ("1 - Combat en cours")
			print ("2 - Alcalins")
			print ("3 - Alcalino-terreux")
			print ("4 - Hallogènes")
			pirnt ("5 - Gaz inertes")
			print ("0 - Retour")
			print (" ")
			choix=input("Choix : ")
		else:
			pass
#################combat
	elif str(choix)=="2":
		print ("1 - ")
		print ("2 - ")
		print ("0 - Retour")
		choix=input("Choix : ")
		os.system('clear')
		if str(choix)=="1":
			print (" ")
		elif str(choix)=="2":
			print (" ")
		else:
			pass
	else:
		print ("Faites votre choix parmi les chiffres proposés")
		pass

