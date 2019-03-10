##### Prodaja knjiga ########

def prodaja():
	lista_knjiga = []
	knjiga = {}
	knjiga["Dostupno"] = 1

	print()
	print("================================")
	print ("Informacije o knjizi: ")
	print("================================")
	print()

	knjiga["Naziv"] = input("Naziv: ")

	zanrovi=["Romani","Autobiografija","Kriminalistika","Strip","Drama","Naucna fantastika"]

	zanr = None
	while zanr is None:
		print()
		print("Dostupni zanrovi: ")
		print()
		for i in range(len(zanrovi)):
			print(str(i+1)+ " ) " + zanrovi[i])

		zanr_id = input("Unesite redni broj: ")
		if zanr_id.isdigit():
			if 0 < int(zanr_id) <= len(zanrovi):
				zanr = zanrovi [int (zanr_id) -1]
				knjiga["Zanr"]=zanr

		else:
			print()
			print("Uneli ste pogresan format rednog broja, on se zapisuje kao broj !")

	print()		
	knjiga["Autor"] = input("Autor: ")

	godina = None
	while godina is None:
		print()
		unos_godine = input("Godina: ")
		if unos_godine.isdigit() and len(unos_godine) <= 4:
			godina = unos_godine
			knjiga["Godina"] = godina

		else:
			print()
			print("Uneli ste pogresan format godine, godina se zapisuje kao broj !")

	cena = None
	while cena is None:
		print()
		unos_cena = input("Cena: ")
		if unos_cena.isdigit():
			cena = unos_cena
			knjiga["Cena"] = cena
			
		else:
			print()
			print ("Uneli ste pogresan format cene, cena se zapisuje kao broj !")
	

	kolicina = None
	while kolicina is None:
		print()
		unos_kolicina = input("Kolicina: ")
		if unos_kolicina.isdigit() and len(unos_kolicina) <3:
			kolicina = unos_kolicina
			knjiga["Kolicina"] = kolicina 

		else:
			print()
			print ("Uneli ste pogresan format, kolicina se zapisuje kao broj !")

	ISBN = None
	while ISBN is None:
		print()
		unos_isbn = input ("ISBN: ")
		if unos_isbn.isdigit() and len(unos_isbn) <7:
			ISBN = unos_isbn
			knjiga["ISBN"] = ISBN

		else:
			print()
			print ("Uneli ste pogresan ISBN format !")

	knjiga["Zavrsna_Cena"] = (int(knjiga["Kolicina"])* int(knjiga["Cena"]))


	lista_knjiga.append(knjiga)

	izgled = "{}|{}|{}|{}|{}|{}|{}|{}|{}\n".format (knjiga["Naziv"], knjiga["Zanr"], knjiga["Autor"], knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"],knjiga["Dostupno"],str(knjiga["Zavrsna_Cena"]) + "0" + " " + "RSD")


	print()
	print()
	print ("Uspesno ste prodali knjigu! ")
	


	x= open("korpa.txt", "a")
	x.write(izgled)
	x.close()

####### Ucitavanje knjiga ##########

def ucitavanje_knjige():
	a = open("korpa.txt", "r")
	knjige = []

	for line in a.readlines():
		knjiga = {}

		podaci = line.strip().split("|")
		knjiga["Naziv"] = podaci [0]
		knjiga["Zanr"] = podaci [1]
		knjiga["Autor"] = podaci [2]
		knjiga["Godina"] = podaci [3]
		knjiga["Cena"] = podaci [4]
		knjiga["Kolicina"] = podaci [5]
		knjiga["ISBN"] = podaci [6]
		knjiga["Dostupno"] = podaci [7]
		knjiga["Zavrsna_Cena"] = podaci [8][:-3]
		
		knjige.append(knjiga)

	return knjige


##### Kupovina iz korpe######

def kupi_korpu():
	knjiga_informacije = ucitavanje_knjige()

	Zavrsna_Cena = 0
	for knjiga in knjiga_informacije:
		Zavrsna_Cena += float(knjiga["Zavrsna_Cena"][:-3])
	print()
	print("Konacna Cena: ")
	print()
	print(str(Zavrsna_Cena) + "0" + "RSD")