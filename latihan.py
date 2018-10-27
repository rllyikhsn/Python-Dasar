def cocacola(uang):
	return uang-3000
	
def granita(uang):
	return uang-1000
	
def tehgelas(uang):
	return uang-2000
	
def menu ():
	uang = int(input("Masukkan Uang Anda : Rp."))
	print("Menu :")
	print("1. Coca-Cola Rp.3000")
	print("2. Granita Rp.1000")
	print("3. Teh Gelas Rp.2000")
	pilihan = int(input("Masukkan angka pilihan anda : "))
	if (pilihan == 1):
		print("Anda telah membeli Coca-Cola seharga Rp.3000")
		print("Uang kembalian Anda = Rp.",cocacola(uang))
	elif (pilihan == 2):
		print("Anda telah membeli Granita seharga Rp.1000")
		print("Uang kembalian Anda = Rp.",granita(uang))
	elif (pilihan == 3):
		print("Anda telah membeli Teh Gelas seharga Rp.2000")
		print("Uang kembalian Anda = Rp.",tehgelas(uang))
	else:
		print("Tidak ada pilihan")
	
menu()
	