def add(no1,no2):				#Function Operasi Penjumlahan
	return no1 + no2			#Mengembalikan nilai no1 dan no 2

def sub(no1,no2):				#Operasi Pengurangan
	return no1 - no2

def mul(no1,no2):				#Operasi Perkalian
	return no1 * no2
	
def div(no1,no2):				#Operasi Pembagian
	return no1 / no2

def ulang():
	ulang = input ("Ingin mengulangi Operasi (Y/T) ?")
	if (ulang != 'Y' and ulang != 'y'):
		exit()
	else:
		main()

def main ():					#fungsi utama pada python
	operation = input ("Operasi yang diinginkan (+,-,*,/) : ")
	if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		#ketidakbenaran operator
		print ("Harap masukan operasi yang sesuai (+,-,*,/)")
		main()
	else:
		no1 = int(input ("Masukkan Bilangan pertama : "))
		no2 = int(input ("Masukkan Bilangan kedua : "))
		if (operation == '+'):
			print ("Hasil Penjumlahan :",add(no1,no2))
			ulang()
		elif (operation == '-'):
			print ("Hasil Pengurangan :",sub(no1,no2))
			ulang()
		elif (operation == '*'):
			print ("Hasil Perkalian :",mul(no1,no2))
			ulang()
		else:
			print ("Hasil Pembagian :",div(no1,no2))
			ulang()
			
main()							#pemanggilan fungsi utama python