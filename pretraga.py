##### Pretraga knjiga po kljucu ######

def pretraga_knjiga(korisnik):
	print("========================")
	print()
	print("Pretraga")
	print()
	print("========================")
	print()
	print("1 - Naziv")
	print("2 - Autor")
	print("3 - Zanr")
	print("4 - ISBN")
	print()
	print()

	broj_pretrage = input("Odaberite opciju: ")

	if broj_pretrage.isdigit():
		
		if broj_pretrage == '1':
			pretraga_naziv(korisnik)
		elif broj_pretrage == '2':
			pretraga_autor(korisnik)
		elif broj_pretrage == '3':
			pretraga_zanr(korisnik)
		elif broj_pretrage == '4':
			pretraga_isbn(korisnik)

		else:
			print("Broj pretrage je nepostojec !")

	else:
		print("Unos treba da bude broj !")

####### Dodavanje knjige u fajl #######

def dodavanje_knjige(knjige):
	a = open("unos_knjige.txt", "w")

	for knjiga in knjige:
		izgled = "{}|{}|{}|{}|{}|{}|{}|{}\n".format (knjiga["Naziv"], knjiga["Zanr"], knjiga["Autor"], knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"],knjiga["Dostupno"])
		a.write(izgled)

###### Ucitavanje knjiga iz fajla ######

def ucitavanje_knjige():
	a = open("unos_knjige.txt", "r")
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
		
		knjige.append(knjiga)

	return knjige

####### Pretraga po nazivu ########

def pretraga_naziv(korisnik):
	baza_knjiga = []
	
	print()
	print()
	a = input("Ukucajte naziv knjige: ")

	knjiga_info = ucitavanje_knjige()

	print("{:^120}".format("Rezultat pretrage: "))
	print("{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^10}".format("Naziv","Zanr","Autor","Godina","Cena","Kolicina","ISBN"))

	broj = 1
	baza_broj = []
	b = False
	for knjiga in knjiga_info:
		if knjiga["Dostupno"] == '1':
			if a.lower() in knjiga["Naziv"].lower():
				baza_knjiga.append(knjiga)
				baza_broj.append(knjiga)
				b = True
				for knjiga in baza_knjiga:
					print(str(broj)+".)"+"{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^10}".format(knjiga["Naziv"], knjiga["Zanr"],knjiga["Autor"],knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"]))
					broj = broj + 1
					baza_knjiga = []

	if b == False:
		print("Ne postoji takav naziv knjige u bazi! ")
		print("Molimo vas pokusajte ponovo")
		pretraga_naziv(korisnik)

	print("Izaberite knjigu iz ponude: ")

	rezultat = None
	while rezultat is None:
		print()
		unos_rezultat = input("Izaberite knjigu: ")
		if unos_rezultat.isdigit():
			rezultat = baza_broj[int(unos_rezultat) - 1]
			print(rezultat)
			if korisnik["Uloga"] == "Admin":
				print("Da li zelite da izmenite knjigu ili obrisete? ")
				a = str(input("Obrisi ili Izmeni? "))
				if a == "obrisi" or a == "Obrisi":
					rezultat["Dostupno"] = "0"
					dodavanje_knjige(knjiga_info)
					print("Uspesno ste obrisali knjigu! ")
				else:
					izmena_knjiga(rezultat)

			else:
				print("Da li zelite da kupite ovu knjigu? ")
				a = input("Da ili Ne? : ")
				if a == "Da" or a == "da":
					racun(rezultat)
				else:
					print("Uspesno ste izasli iz prodavnice !")

		else:
			print("Unos mora biti broj !")

###### Pretraga po autoru ########

def pretraga_autor(korisnik):
	baza_knjiga = []
	
	a = input("Ukucajte naziv autora po kom zelite da trazite knjigu: ")

	knjiga_info = ucitavanje_knjige()

	print("{:^120}".format("Rezultat pretrage: "))
	print("{:-^20}{:-^25}{:-^15}{:-^12}{:-^8}{:-^20}{:-^10}".format("Naziv","Zanr","Autor","Godina","Cena","Kolicina","ISBN"))

	broj = 1
	baza_broj = []
	b = False
	for knjiga in knjiga_info:
		if knjiga["Dostupno"] == "1":
			if a.lower() in knjiga["Autor"].lower():
				baza_knjiga.append(knjiga)
				baza_broj.append(knjiga)
				b = True
				for knjiga in baza_knjiga:
					print(str(broj)+".)"+"{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^10}".format(knjiga["Naziv"], knjiga["Zanr"],knjiga["Autor"],knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"]))
					broj = broj + 1
					baza_knjiga = []

	if b == False:
		print("Ne postoji takav autor u bazi! ")
		print("Molimo vas pokusajte ponovo !")
		pretraga_autor(korisnik)

	print("Izaberite knjigu iz ponude: ")

	rezultat = None
	while rezultat is None:
		print()
		unos_rezultat = input("Izaberite knjigu: ")
		if unos_rezultat.isdigit():
			rezultat = baza_broj[int(unos_rezultat) - 1]
			print(rezultat)
			if korisnik["Uloga"] == "Admin":
				print("Da li zelite da izmenite knjigu ili obrisete? ")
				a = str(input("Obrisi ili Izmeni? "))
				if a == "obrisi" or a == "Obrisi":
					rezultat["Dostupno"] = "0"
					dodavanje_knjige(knjiga_info)
					print("Uspesno ste obrisali knjigu! ")
				else:
					izmena_knjiga(rezultat)

			else:
				print("Da li zelite da kupite ovu knjigu? ")
				a = input("Da ili Ne? : ")
				if a == "Da" or a == "da":
					racun(rezultat)
				else:
					print("Uspesno ste izasli iz prodavnice !")

		else:
			print("Unos mora biti broj !")

####### Pretraga po zanru knjige ########

def pretraga_zanr(korisnik):
	baza_knjiga = []
	
	a = input("Ukucajte zanr knjige: ")

	knjiga_info = ucitavanje_knjige()

	print("{:^120}".format("Rezultat pretrage: "))
	print("{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^10}".format("Naziv","Zanr","Autor","Godina","Cena","Kolicina","ISBN"))

	broj = 1
	baza_broj = []
	b = False
	for knjiga in knjiga_info:
		if knjiga["Dostupno"] == "1":
			if a.lower() in knjiga["Zanr"].lower():
				baza_knjiga.append(knjiga)
				baza_broj.append(knjiga)
				b = True
				for knjiga in baza_knjiga:
					print(str(broj)+".)"+"{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^10}".format(knjiga["Naziv"], knjiga["Zanr"],knjiga["Autor"],knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"]))
					broj = broj + 1
					baza_knjiga = []

	if b == False:
		print("Ne postoji zadat zanr knjige u bazi! ")
		print("Molimo vas pokusajte ponovo !")
		pretraga_zanr(korisnik)

	print("Izaberite knjigu iz ponude: ")

	rezultat = None
	while rezultat is None:
		print()
		unos_rezultat = input("Izaberite knjigu: ")
		if unos_rezultat.isdigit():
			rezultat = baza_broj[int(unos_rezultat) - 1]
			print(rezultat)
			if korisnik["Uloga"] == "Admin":
				print("Da li zelite da izmenite knjigu ili obrisete? ")
				a = str(input("Obrisi ili Izmeni? "))
				if a == "obrisi" or a == "Obrisi":
					rezultat["Dostupno"] == "0"
					dodavanje_knjige(knjiga_info)
					print("Uspesno ste obrisali knjigu! ")
				else:
					izmena_knjiga(rezultat)

			else:
				print("Da li zelite da kupite ovu knjigu? ")
				a = input("Da ili Ne? : ")
				if a == "Da" or a == "da":
					racun(rezultat)
				else:
					print("Uspesno ste izasli iz prodavnice !")

		else:
			print("Unos mora biti broj !")


###### Pretraga po ISBN-u #######

def pretraga_isbn(korisnik):
	baza_knjiga = []
	
	a = input("Ukucajte ISBN knjige: ")

	knjiga_info = ucitavanje_knjige()

	print("{:^120}".format("Rezultat pretrage: "))
	print("{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^2}".format("Naziv","Zanr","Autor","Godina","Cena","Kolicina","ISBN"))

	broj = 1
	baza_broj = []
	b = False
	for knjiga in knjiga_info:
		if knjiga["Dostupno"] == "1":
			if a.lower() in knjiga["ISBN"].lower():
				baza_knjiga.append(knjiga)
				baza_broj.append(knjiga)
				b = True
				for knjiga in baza_knjiga:
					print(str(broj)+".)"+"{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^10}".format(knjiga["Naziv"], knjiga["Zanr"],knjiga["Autor"],knjiga["Godina"],knjiga["Cena"],knjiga["Kolicina"],knjiga["ISBN"]))
					broj = broj + 1
					baza_knjiga = []

	if b == False:
		print("Ne postoji zadat ISBN knjige u bazi! ")
		print("Molimo vas pokusajte ponovo")
		pretraga_isbn(korisnik)

	print("Izaberite knjigu iz ponude: ")

	rezultat = None
	while rezultat is None:
		print()
		unos_rezultat = input("Izaberite knjigu: ")
		if unos_rezultat.isdigit():
			rezultat = baza_broj[int(unos_rezultat) - 1]
			print(rezultat)
			if korisnik["Uloga"] == "Admin":
				print("Da li zelite da izmenite knjigu ili obrisete? ")
				a = str(input("Obrisi ili Izmeni? "))
				if a == "obrisi" or a == "Obrisi":
					rezultat["Dostupno"] == "0"
					dodavanje_knjige(knjiga_info)
					print("Uspesno ste obrisali knjigu! ")
				else:
					izmena_knjiga(rezultat)

			else:
				print("Da li zelite da kupite ovu knjigu? ")
				a = input("Da ili Ne? : ")
				if a == "Da" or a == "da":
					racun(rezultat)
				else:
					print("Uspesno ste izasli iz prodavnice !")

		else:
			print("Unos mora biti broj !")

##### Deo za izmenu knjiga ######

def izmena_knjiga(rezultat):
	print("=======================")
	print()
	print("Izmena unosa podataka knjiga")
	print()
	print("========================")
	print()
	print (" 1 - Izmena naziva knjige")
	print (" 2 - Izmena zanra knjige")
	print (" 3 - Izmena autora knjige")
	print (" 4 - Izmena godine izdavanja knjige")
	print (" 5 - Izmena cene knjiga")
	print (" 6 - Izmena kolicinskog stanja")
	print (" 7 - Izmena ISBN broja")
	print()

	opcija_broj = input("Unesite broj opcije koju zelite da promenite: ")
	if opcija_broj.isdigit():
		if opcija_broj == '1':
			izmena_naziv(rezultat)
		elif opcija_broj == '2':
			izmena_zanr(rezultat)
		elif opcija_broj == '3':
			izmena_autor(rezultat)
		elif opcija_broj == '4':
			izmena_godine(rezultat)
		elif opcija_broj == '5':
			izmena_cene(rezultat)
		elif opcija_broj == '6':
			izmena_kolicina(rezultat)
		elif opcija_broj == '7':
			izmena_isbn(rezultat)
		else:
			print("Uneli ste nepostojec broj !")
	else:
		print("Unos mora biti broj !")

#### Izmena po nazivu u bazi #####

def izmena_naziv(rezultat):
	knjiga_info = ucitavanje_knjige()
	print()
	a = input("Ukucajte novo ime za ovu knjigu: ")
	print()
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Naziv"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili ime knjige !")
			print()

##### Izmena po zanru u bazi #####

def izmena_zanr(rezultat):
	print()
	print("1 - Romani")
	print("2 - Autobiografija")
	print("3 - Kriminalistika")
	print("4 - Stripovi")
	print("5 - Drama")
	print("6 - Naucna fanstastika")
	print()

	zanr_id = input("Unesite redni broj opcije koju zelite: ")
	if zanr_id.isdigit():
		if zanr_id == '1':
			a = "Romani"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")	

		elif zanr_id == '2':
			a = "Autobiografija"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")
			
		elif zanr_id == '3':
			a = "Kriminalistika"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")

		elif zanr_id == '4':
			a = "Stripovi"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")
		elif zanr_id == '5':
			a = "Drama"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")

		elif zanr_id == '6':
			a = "Naucna fantastika"
			knjiga_info = ucitavanje_knjige()
			for knjiga in knjiga_info:
				if knjiga["ISBN"] == rezultat["ISBN"]:
					knjiga["Zanr"] = a
					dodavanje_knjige(knjiga_info)
					print()
					print("Uspesno ste promenili zanr knjige !")

	else:
		print("Unos mora biti broj !")

###### Izmena po autoru u bazi ######

def izmena_autor(rezultat):
	knjiga_info = ucitavanje_knjige()
	a = input("Ukucajte novog autora za ovu knjigu: ")
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Autor"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili autora knjige !")

##### Izmena godina izdavanja knjiga u bazi #####

def izmena_godine(rezultat):
	knjiga_info = ucitavanje_knjige()
	a = input("Ukucajte novu godinu izdavanja za ovu knjigu: ")
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Godina"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili godinu izdavanja knjige !")

##### Izmena cene knjiga u bazi #####

def izmena_cene(rezultat):
	knjiga_info = ucitavanje_knjige()
	a = input("Ukucajte novu cenu za ovu knjigu: ")
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Cena"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili cenu knjige !")

##### Izmena kolicinskog stanja knjiga u bazi #######

def izmena_kolicina(rezultat):
	knjiga_info = ucitavanje_knjige()
	a = input("Ukucajte novo kolicinsko stanje za ovu knjigu: ")
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Kolicina"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili kolicinsko stanje knjige !")


##### Izmena jedinstvenog ISBN broja knjiga u bazi ######

def izmena_isbn(rezultat):
	knjiga_info = ucitavanje_knjige()
	a = input("Ukucajte nov ISBN za ovu knjigu: ")
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"] and a == 6:
			knjiga["ISBN"] = a
			dodavanje_knjige(knjiga_info)
			print()
			print("Uspesno ste promenili ISBN knjige !")


##### Racun #####

def racun(rezultat):
	print("=====================")
	print()
	print("Vi zelite da kupite ovu knjigu? ")
	print()
	print("=====================")
	print(rezultat)
	print()
	print("Vi trebate da platite "+ rezultat["Cena"]+",00" "RSD")

	knjiga_info = ucitavanje_knjige()
	for knjiga in knjiga_info:
		if knjiga["ISBN"] == rezultat["ISBN"]:
			knjiga["Kolicina"] = (int(rezultat["Kolicina"])-1)
			dodavanje_knjige(knjiga_info)
	print()		
	print("Uspesno ste istampali racun !")
	










