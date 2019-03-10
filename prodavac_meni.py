from pretraga import *
from prodaja import *

####### Prodavac meni ########

def prodavac_meni(korisnik):
	print()
	print('=====================')
	print ("Prodavac Meni")
	print('=====================')
	print()
	print()
	print ("Odaberite opciju:")

	print (" 1 - Pretraga knjiga")
	print (" 2 - Kupi knjigu")
	print (" 3 - Kupi iz korpe")
	print (" 4 - Izlaz")
	print()


	opcije = str(input("Unesite redni broj:"))
	if opcije == '1':
		pretraga_knjiga(korisnik)
		prodavac_meni(korisnik)
	elif opcije == '2':
		pretraga_knjiga(korisnik)
	elif opcije == '3':
		kupi_korpu()
		prodavac_meni(korisnik)
	elif opcije == '4':
		print()
		print ("Uspesno ste izasli !")
	else:
		print ("Ova funkcija ne postoji")
		print ("Molimo vas pokusajte ponovo")
		prodavac_meni(korisnik)