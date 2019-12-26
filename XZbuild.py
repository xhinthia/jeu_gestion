import random
import os
import sys
from fonctions import *

a=1
while a==1:
	choix=menu_3_choix("MENU PRINCIPAL","Expédition","Quartier royal","Quartier marchand","Quitter")
	if str(choix)=="0":
		quit()
	elif str(choix)=="1":
		b=1
		while b==1:
			choix=menu_3_choix("EXPEDITION","Combat","Minage","Infiltration","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("COMBAT","Combattre","Siège","Composition","Retour")
			elif str(choix)=="2":
				choix=menu_3_choix("MINAGE","Miner","Prospection","Puits de mine","Retour")
			elif str(choix)=="3":
				choix=menu_3_choix("INFILTRATION","Voler des ressources","Tuer le chef","Espionnage","Retour")
			else:
				pass
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_3_choix("QUARTIER ROYAL","Archives","Caserne","Eglise","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("ARCHIVES","Revue des troupes","Rapports de combat","Coffre-fort","Retour")
			elif str(choix)=="2":
				choix=menu_3_choix("CASERNE","Entraînement militaire","Entraînement tactique","Investir","Retour")
			elif str(choix)=="3":
				choix=menu_3_choix("EGLISE","Don d'Arès","Don d'Héphaïstos","Don d'Hermès","Retour")
			else:
				pass
	elif str(choix)=="3":
		b=1
		while b==1:
			choix=menu_3_choix("QUARTIER MARCHAND","Marché noir","Hôtel des ventes","Joaillerie","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("MARCHE NOIR","Adrenaline","Pioche de Stakhanov","Potion d'invisibilité","Retour")
			elif str(choix)=="2":
				choix=menu_3_choix("HOTEL DES VENTES","Acheter des pierres","Vendre des pierres","Investir","Retour")
			elif str(choix)=="3":
				choix=menu_3_choix("JOAILLERIE","Fabriquer","Polir","Investir","Retour")
			else:
				pass
	else:
		pass

