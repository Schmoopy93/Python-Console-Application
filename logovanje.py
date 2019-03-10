from menadzer_meni import*
from prodavac_meni import*

##### Ucitavanje korisnika iz fajla #######

def ucitavanje_korisinka():
	a = open("korisnici.txt","r")

	korisnici = []
	for line in a.readlines():
		korisnik = {}
		prikaz = line.strip().split("|")
		korisnik["Korisnicko ime"] = prikaz [0] 
		korisnik["Lozinka"] = prikaz [1]
		korisnik["Ime"] = prikaz [2]
		korisnik["Prezime"] = prikaz [3]
		korisnik["Uloga"] = prikaz [4]
		korisnik["JMBG"] = prikaz [5]

		korisnici.append(korisnik)
		
	return korisnici

####### Funkcija za logovanje ##########

def logovanje():

	print()
	a = input("Korisnicko ime: ")
	b = input("Lozinka: ")

	korisnik_podaci = ucitavanje_korisinka()

	pronadjen_korisnik = False

	for korisnik in korisnik_podaci:
		if a == korisnik["Korisnicko ime"] and b == korisnik["Lozinka"]:
			print()
			print("Uspesno ste se ulogovali kao: " + korisnik["Ime"]+" "+ korisnik["Prezime"])
			print("Uloga: " + korisnik["Uloga"])
			print()

			pronadjen_korisnik = True

			if korisnik["Uloga"] == "Admin":
				menadzer_meni(korisnik)
			else:
				prodavac_meni(korisnik)

	if not pronadjen_korisnik:
		print("Uneli ste pogresno korisnicko ime i lozinku !")
		logovanje()
