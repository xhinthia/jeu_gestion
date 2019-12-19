import random
import os
import sys

def menu_3_choix(titre,choix_1,choix_2,choix_3,choix_0):
	os.system("clear")
	print ("******************************")
	print ("")
	print ("	"+str(titre))
	print ("")
	print ("******************************")
	print (" ")
	print ("<><><><><><><><><><><><><><><>")
	print ("")
	print ("1 > "+str(choix_1))
	print ("")
	print ("2 > "+str(choix_2))
	print ("")
	print ("3 > "+str(choix_3))
	print ("")
	print ("0 > "+str(choix_0))
	print ("")
	print ("<><><><><><><><><><><><><><><>")
	choix=input()
	return choix