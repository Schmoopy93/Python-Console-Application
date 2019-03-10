from unos_knjiga import*
from pretraga import*
from prodaja import*

###### Menadzer meni #########

def menadzer_meni(korisnik):
	print()
	print('=====================')
	print ("Menadzer Meni")
	print('=====================')
	print()
	print()
	print ("Odaberite opciju:")

	print (" 1 - Unos knjiga")
	print (" 2 - Pretraga knjiga")
	print (" 3 - Stavi u korpu")
	print (" 4 - Izlaz")
	print()


	opcije = str(input("Unesite redni broj:"))
	if opcije == '1':
		unos_knjiga()
		menadzer_meni(korisnik)
	elif opcije == '2':
		pretraga_knjiga(korisnik)
	elif opcije == '3':
		prodaja()
		menadzer_meni(korisnik)
	elif opcije == '4':
		print()
		print ("Uspesno ste izasli !")
	else:
		print ("Ova funkcija ne postoji")
		print ("Molimo vas pokusajte ponovo")
		menadzer_meni()	




